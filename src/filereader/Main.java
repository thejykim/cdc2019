package filereader;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws FileNotFoundException {

		// Change the file URL to your location
		File text = new File("C:/Users/jyk/Downloads/police-incident-reports-written.txt");
		
		Scanner scan = new Scanner(text).useDelimiter(";");
		
		// Goes through the header because we don't need it
		
		for (int i = 0; i < 17; i++) {
			scan.next();
		}
		// System.out.println(scan.next());
		System.out.println(scan.next());
		
		// Goes through each line of the police record
		
		while(scan.hasNextLine()) {
			for (int i = 0; i < 16; i++) {
				scan.next();
			}
			System.out.println(scan.next());
		}
		
		
		scan.close();
	}

}
