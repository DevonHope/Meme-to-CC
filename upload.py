#upload to photos
import os
from os.path import join, dirname
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from httplib2 import Http
from oauth2client import file, client, tools
import json
import pickle

def getAlbumID(album_name):
    SCOPES = 'https://www.googleapis.com/auth/photoslibrary.sharing'
    if album_name == "":
        album_name = "vroom"
        print("predefined album used: vroom")

    album = album_name

    g_api = 'GP-API-credentials.json'
    
    store = file.Storage(join(dirname(__file__), 'token-for-google.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(join(dirname(__file__), g_api), SCOPES)
        creds = tools.run_flow(flow, store)
    google_photos = build('photoslibrary', 'v1', http=creds.authorize(Http()))

    day, month, year = ('0', '3', '2020')  # Day or month may be 0 => full month resp. year
    date_filter = [{"day": day, "month": month, "year": year}]  # No leading zeroes for day an month!
    nextpagetoken = 'Dummy'
    while nextpagetoken != '':
        nextpagetoken = '' if nextpagetoken == 'Dummy' else nextpagetoken
        results = google_photos.albums().list(pageSize=5, fields="nextPageToken,albums(id,title)").execute()
        #results = google_photos.mediaItems().search(
        #        body={"filters":  {"dateFilter": {"dates": [{"day": day, "month": month, "year": year}]}},
        #              "pageSize": 10, "pageToken": nextpagetoken}).execute()
        # The default number of media items to return at a time is 25. The maximum pageSize is 100.
        items = results.get('albums', [])
        nextpagetoken = results.get('nextPageToken', '')
        for item in items:
            if(item['title'] == album):
                print(item['id'])
                return item['id']
            else: 
                print("album not found")
                nextpagetoken == ''
                break
            #print(items['album'])
            #print(f"{item['filename']} {item['mimeType']} '{item.get('description', '- -')}'" f" {item['mediaMetadata']['creationTime']}\nURL: {item['productUrl']}")

def uploadImage(name, album):
    SCOPES = 'https://www.googleapis.com/auth/photoslibrary.sharing'
    album = album_name
    albumID = getAlbumID(album_name)
    g_api = 'GP-API-credentials.json'
    
    store = file.Storage(join(dirname(__file__), 'token-for-google.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(join(dirname(__file__), g_api), SCOPES)
        creds = tools.run_flow(flow, store)
    google_photos = build('photoslibrary', 'v1', http=creds.authorize(Http()))

    try:
        basename = os.path.basename(name)
        headers = {'Authorization': 'Bearer ' + self.client_token.token, 
                    'Content-type': 'application/octet-stream',
                    'X-Goog-Upload-Protocol': 'raw',
                    'X-Goog-File-Name': basename}

        image_data = open(img_name, 'rb').read()
        response_upload = requests.post(upload.upload_base_url, headers=headers, data=image_data)
        print(response_upload.content.decode('utf-8'))
        return response_upload.content.decode('utf-8')

    except Exception as e:
        print(e)
        return None


    day, month, year = ('0', '3', '2020')  # Day or month may be 0 => full month resp. year
    date_filter = [{"day": day, "month": month, "year": year}]  # No leading zeroes for day an month!
    nextpagetoken = 'Dummy'
    while nextpagetoken != '':
        nextpagetoken = '' if nextpagetoken == 'Dummy' else nextpagetoken
        results = google_photos.albums().list(pageSize=5, fields="nextPageToken,albums(id,title)").execute()
        #results = google_photos.mediaItems().search(
        #        body={"filters":  {"dateFilter": {"dates": [{"day": day, "month": month, "year": year}]}},
        #              "pageSize": 10, "pageToken": nextpagetoken}).execute()
        # The default number of media items to return at a time is 25. The maximum pageSize is 100.
        items = results.get('albums', [])
        nextpagetoken = results.get('nextPageToken', '')
        for item in items:
            if(item['title'] == album):
                print(item['id'])
                return item['id']

def emptyAlbum():
    print()

def service(g_api, api_name, api_v, *scopes):
    s_file = g_api
    service_name = api_name
    v = api_v
    scope = [scope for scope in scopes[0]]

    cred = None

    pickle_f = f'token_{service_name}_{v}.pickle'

    if os.path.exists(pickle_f):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)
    '''
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(s_file, scope)
            cred = flow.run_local_server()

        with open(pickle_f, 'wb') as token:
            pickle.dump(cred, token)
    '''
    g_api = 'GP-API-credentials.json'
    
    store = file.Storage(join(dirname(__file__), 'token-for-google.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(join(dirname(__file__), g_api), scope)
        creds = tools.run_flow(flow, store)
    google_photos = build(api_name, api_v, http=creds.authorize(Http()))

    try:
        service = build(service_name, v, credentials=cred)
        print(service_name, 'service created successfully')
        return service

    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

class upload:
    upload_base_url = 'https://photoslibrary.googleapis.com/v1/uploads'
    g_api = 'GP-API-credentials.json'
    API_NAME = 'photoslibrary'
    API_V = 'v1'
    scopes = ['https://www.googleapis.com/auth/photoslibrary',
              'https://www.googleapis.com/auth/photoslibrary.sharing']

    def __init__(self, album_name):
        
        self.initService()
        #self.upload_im(img_name, album_name)

    def initService(self):
        self.service = service(upload.g_api, upload.API_NAME, upload.API_V, upload.scopes)
        self.client_token = json.load(open('token-for-google.json', 'rb'))

    def upload_im(self, img_name, album_name):
        try:
            basename = os.path.basename(img_name)
            headers = {'Authorization': 'Bearer ' + self.client_token.token, 
                        'Content-type': 'application/octet-stream',
                        'X-Goog-Upload-Protocol': 'raw',
                        'X-Goog-File-Name': basename}

            image_data = open(img_name, 'rb').read()
            response_upload = requests.post(upload.upload_base_url, headers=headers, data=image_data)
            print(response_upload.content.decode('utf-8'))
            return response_upload.content.decode('utf-8')

        except Exception as e:
            print(e)
            return None