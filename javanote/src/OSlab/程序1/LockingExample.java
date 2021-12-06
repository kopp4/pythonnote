package OSlab.程序1;

import java.io.*;
import java.nio.channels.*;

public class LockingExample {
	
	public static final boolean EXCLUSIVE = false;
	public static final boolean SHARED = true;

	public static void main(String[] args) throws IOException {
		
		FileLock sharedLock = null;
		FileLock exclusiveLock = null;
		
		try{
			RandomAccessFile raf = new RandomAccessFile("file.txt","rw");
			FileChannel ch = raf.getChannel();
			
			exclusiveLock = ch.lock(0, raf.length()/2, EXCLUSIVE);
			raf.seek(5);
			raf.writeBytes("Hello World!");
			exclusiveLock.release();
			
			sharedLock = ch.lock(raf.length()/2, raf.length()/2, SHARED);
			raf.seek(raf.length()/2+1);
			String str = raf.readLine();
			System.out.println(str);
			sharedLock.release();
		
		}catch(java.io.IOException ioe){
			System.err.println(ioe);
		}
		finally{
			if(exclusiveLock!=null)
				exclusiveLock.release();
			if(sharedLock != null)
				sharedLock.release();
		}

	}

}
