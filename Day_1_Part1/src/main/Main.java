package main;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	private static ArrayList<Integer> Array1 =new ArrayList<>();
	private static ArrayList<Integer> Array2 =new ArrayList<>();
	public static void main(String[] args) {
		getArrayInt();
		Collections.sort(Array1);
		Collections.sort(Array2);
		System.out.println(getResult());
	}

	public static void getArrayInt() {
		File file=new File("src/input.txt");
		try {
			Scanner reader=new Scanner(file);
			while(reader.hasNextLine()) {
				String data=reader.nextLine();
				String[] stringArray=data.split("   ");
				Array1.add(Integer.parseInt(stringArray[0]));
				Array2.add(Integer.parseInt(stringArray[1]));
			}
			reader.close();
		} catch (FileNotFoundException e) {

			e.printStackTrace();
		}
	}
		
		public static int getResult() {
			int result=0;
			for(int i=0;i<Array1.size();i++) {
				int temp=Array1.get(i)-Array2.get(i);
				result+=Math.abs(temp);
			}
			return result;
		}
}
