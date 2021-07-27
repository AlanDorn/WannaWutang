package wannaWutangPackage;

import java.net.URL;
import java.net.URLConnection;
import java.net.HttpURLConnection;
import java.net.*;
import java.io.*;


public class WutangClass
{

	public static void main(String[] args) throws Exception	{
		// TODO Auto-generated method stub
		
		URL myURL = new URL("https://www.mess.be/inickgenwuname.php");
		URLConnection myURLConnection = myURL.openConnection();
		myURLConnection.connect();
		
		BufferedReader in = new BufferedReader(new InputStreamReader(myURLConnection.getInputStream()));
		
		String inputLine = " ";
		
		while((inputLine = in.readLine()) != null)
			System.out.println(inputLine);
		in.close();
		
	}
		
		
	
}


