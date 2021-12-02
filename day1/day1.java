import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day1
{
  public static void main(String[] args)
  {
    String prev="";
    int counter=0;
    int increases=0;
    try
    {
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);

      while (myReader.hasNextLine())
      {
        String data = myReader.nextLine();
        if (counter!=0 && Integer.parseInt(data)>Integer.parseInt(prev))
        {
          increases++;
        }
        prev=data;
        counter++;
      }
      myReader.close();
    }
    catch (FileNotFoundException e)
    {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    System.out.println(increases);
  }
}
