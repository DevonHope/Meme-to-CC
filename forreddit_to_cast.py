#reddit to chromecast meme grabber
#
#Desc:
#	To grab memes from any subreddit for memes and send them to a designated
#	google photos folder for a users API key
#
#USE:
#	python3 forreddit_to_cast.py -s memes -l 20
#	arguments:
#		--sub or -s: for choosing your sub. ex memes or highqualitymemes
#		--limit or -l: for choosing the limit of images that are downloaded
#									 ex 10,20,30,50,100
#
#!/usr/bin/env python3
import requests
import praw
import pandas as pd
import os
import argparse
import random
import urllib.error
import sys
import requests
import json
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageFile
from pprint import pprint
from urllib.request import urlretrieve


# Print iterations progress
def printPB (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    '''
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    '''
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def getmemes(posts,sub):
	a_ext = ["jpg","png"]

	#change directory to meme folder
	fold = 'resources/sub_'+sub
	fixfold = 'resources/fixed_'+sub
	if not os.path.exists(fold):
		os.makedirs(fold)
	if not os.path.exists(fixfold):
		os.makedirs(fixfold)
	os.chdir(fold)

	#num of memes downloaded
	num_me = 0

	printPB(0, len(posts['url']), prefix='Dowloading:',suffix='Done',length=50)
	#get url json for each post
	for i, url in enumerate(posts['url']):
		name = url.split('/')
		if (len(name) == 4):
			name = name[3]
			if('.' in name):
				ext = name.split('.')[1]
				if(ext in a_ext):
					if(len(ext) <= 3):
						#print('Downloading image: '+name)
						printPB(i+1,len(posts['url']), prefix='Dowloading:',suffix='Done',length=50)
						#try and except for error handling
						try:
								urlretrieve(url, name)
						except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')
						except urllib.error.HTTPError as e: ResponseData = e.read().decode("utf8", 'ignore')
						except KeyboardInterrupt:
							print()
							print('UGH! I almost dropped my croissant!')
							try:
								sys.exit(0)
							except SystemExit:
								os._exit(0)
						num_me+=1
	print()
	print(str(num_me) + ' memes downloaded')
	os.chdir("../..")

def formatMemes(sub):
	ImageFile.LOAD_TRUNCATED_IMAGES = True
	bgdir = "resources/bgmemes"
	memedir = "resources/sub_"+sub
	fixme = "resources/fixed_"+sub
	a_ext = ["jpg","png"]

	#get all background images
	allbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]

	#convert all background images to jpg for RGBA formatting in Pillow
	for bg in allbg:
		ext = bg.split('.')[1]
		if (ext != "jpg"):
			#convert to jpg
			p_bg = bgdir+"/"+bg
			im = Image.open(p_bg)
			rgb_im = im.convert('RGB')

			#remove old file
			os.remove(p_bg)

			newname = p_bg.partition('.')[0] + ".jpg"
			rgb_im.save(newname)

	#get all memes
	allmeme = [i for i in listdir(memedir) if isfile(join(memedir, i))]
	newbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]
	print()
	printPB(0, len(allmeme), prefix='Fixing:',suffix='Done',length=50)
	for i, m in enumerate(allmeme):
		m_ext = m.split('.')[1]
		if(m_ext in a_ext):
			#get path for random background meme
			ran = random.choice(newbg)

			#get paths & convert images to rgb
			bgpath = bgdir+"/"+ran
			mepath = memedir+"/"+m

			#open images
			try:
				bg = Image.open(bgpath)
				me = Image.open(mepath)
			except Image.UnidentifiedImageError as e: print(e)


			o = True
			while(o):
				#find ratios
				rat_w = (me.width / bg.width) * 100
				rat_h = (me.height / bg.height) * 100

				#if the ratio is below %50 find smaller background
				if(rat_h <= 75 and rat_w <= 75):
					r_val = 1.25
					me = me.resize((round(me.size[0]*r_val), round(me.size[1]*r_val)))

				elif(me.width > bg.width or me.height > bg.height):
					#resize memes that are too big for any background
					#resizes them to %80
					r_value = .80
					#print('resized ' +m)
					if(rat_h >= 100 and rat_w >= 100):
						me = me.resize((round(me.size[0]*r_value), round(me.size[1]*r_value)))
					elif(rat_w >= 100):
						me = me.resize((round(me.size[0]*r_value), round(me.size[1]*1)))
					elif(rat_h >= 100):
						me = me.resize((round(me.size[0]*1), round(me.size[1]*r_value)))
				#make sure meme is smaller than bg
				elif (bg.width < me.width and bg.height < me.height):
					ran = random.choice(newbg)
					bgpath = bgdir+"/"+ran
					bg = Image.open(bgpath)

				elif(bg.width >= me.width and bg.height >= me.height):
					printPB(i+1, len(allmeme), prefix='Formatting:',suffix='Done',length=50)
					#print('Fixing image '+m)
					o = False
					#make backup copy
					back = bg.copy()

					#get middle of image
					pos = ((back.width - me.width)// 2,(back.height - me.height)//2)

					back.paste(me, pos)
					newname = fixme+"/c_"+str(m)
					back.save(newname)

def getposts(sub, multi, l):
	def_s = 'memes'
	def_l = 5

	#read OAUTH key from separate file
	A_path = 'redditAPI.txt'
	
	#open json api file
	with open(A_path, 'r') as api_file:
		data = api_file.read()
	
	#parse file
	j_obj = json.loads(data)

	#get keys from json obj
	API = j_obj['API-ID']
	Secret = j_obj['API-Secret']
	usr_a = j_obj['User-Agent']
	uName = j_obj['Username']
	pswd = j_obj['Password']

	r = praw.Reddit(client_id= API, \
					client_secret= Secret, \
					user_agent = usr_a, \
					username = uName, \
					password = pswd)

	#get all posts from specified subreddit
	posts = []

	if(multi is None):
		if(sub is None and l is None):
			print('default limit used: ' + str(def_l))
			print('default sub used: ' + def_s)
			sub = def_s
			li = def_l
		elif(sub is None):
			print('default sub used: ' + def_s)
			sub = def_s
			li = int(l)
		elif(l is None):
			print('default limit used: ' + str(def_l))
			li = def_l
		else:
			li = int(l)

		sr = r.subreddit(sub).hot(limit=li)
	else:
		sub = multi
		if(l is None):
			print('default limit used: ' + str(def_l))
			li = def_l
		else:
			li = int(l)

		sr = r.multireddit(uName, sub).hot(limit=li)


	for post in sr:
		posts.append([post.title, \
					post.score, \
					post.id, \
					post.subreddit, \
					post.url, \
					post.num_comments, \
					post.selftext, \
					post.created])

	posts = pd.DataFrame(posts,columns=['title', \
										'score', \
										'id', \
										'subreddit', \
										'url', \
										'num_comments', \
										'body', \
										'created'])

	return {'po':posts,'sub':sub}

def main():

	#get sub and limit from arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('--sub', '-s')
	parser.add_argument('--multi', '-m')
	parser.add_argument('--limit','-l')
	args = parser.parse_args()
	sub = args.sub
	l = args.limit
	mult = args.multi

	dic = getposts(sub, mult, l)

	#print(posts)
	getmemes(dic['po'],dic['sub'])
	formatMemes(dic['sub'])

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print()
		print('UGH! I almost dropped my croissant!')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
