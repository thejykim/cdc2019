package filereader;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.*;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {

		// Change the file URL to your location
		File text = new File("C:/Users/jyk/Downloads/police-incident-reports-written.txt");
		
		Scanner scan = new Scanner(text).useDelimiter(";");
		
		// Initializes writer
		
		try(FileWriter fw = new FileWriter("C:/Users/jyk/Downloads/output1.txt", true);
		    BufferedWriter bw = new BufferedWriter(fw);
		   PrintWriter out = new PrintWriter(bw)) {
			
			// Goes through the header because we don't need it
			
			for (int i = 0; i < 17; i++) {
				scan.next();
			}
			// System.out.println(scan.next());
			out.println(scan.next());
			
			// Goes through each line of the police record
			
			while(scan.hasNextLine()) {
				for (int i = 0; i < 16; i++) {
					scan.next();
				}
				out.println(scan.next());
			}
					    
			} catch (IOException e) {
				// exception handling left as an exercise for the reader
		}
		
		scan.close();
		
		
		// output 2 file
		
		// Change the file URL to your location
		File text2 = new File("C:/Users/jyk/Downloads/output1.txt");
				
		Scanner scan2 = new Scanner(text2).useDelimiter("CHPD");
		
		try(FileWriter fw2 = new FileWriter("C:/Users/jyk/Downloads/output2.txt", true);
			    BufferedWriter bw2 = new BufferedWriter(fw2);
			   PrintWriter out2 = new PrintWriter(bw2)) {
		
			out2.print(scan2.next().substring(2));
			
			while(scan2.hasNext()) {
				out2.print(scan2.next());
			}
					    
		} catch (IOException e) {
			// exception handling left as an exercise for the reader
		}		
		
		scan2.close();
		
	}

}
