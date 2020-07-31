package upload;

import java.io.File;

public class uploadTool{
	public static void upload(File file){
		// Open the file and automatically close it after upload
			try (RandomAccessFile file = new RandomAccessFile(file, "r")) {
				// Create a new upload request
				UploadMediaItemRequest uploadRequest =
						UploadMediaItemRequest.newBuilder()
										// The media type (e.g. "image/png")
										.setMimeType(mimeType)
										// The file to upload
										.setDataFile(file)
								.build();
				// Upload and capture the response
				UploadMediaItemResponse uploadResponse = photosLibraryClient.uploadMediaItem(uploadRequest);
				if (uploadResponse.getError().isPresent()) {
					// If the upload results in an error, handle it
					Error error = uploadResponse.getError().get();
				} else {
					// If the upload is successful, get the uploadToken
					String uploadToken = uploadResponse.getUploadToken().get();
					// Use this upload token to create a media item
				}
			} catch (ApiException e) {
				// Handle error
				System.out.println("API Error: "+e);
			} catch (IOException e) {
				// Error accessing the local file
				System.out.println("IO Error: "+e);
			}
	}
}