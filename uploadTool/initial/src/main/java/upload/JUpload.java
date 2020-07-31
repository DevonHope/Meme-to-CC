package upload;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

// loop around this to get files from each folder of memes
public class JUpload{
	public static void main(String args[]) throws IOException{
		//Creating a File object for directory
		File directoryPath = new File("resources/fixed_memes");
		//List of all files and directories
		String contents[] = directoryPath.list();
		System.out.println("List of files and directories in the specified directory:");
		for(int i=0; i<contents.length; i++) {
			System.out.println(contents[i]);
			uploadTool up = new upload(contents[i]);
		}
	}
}
