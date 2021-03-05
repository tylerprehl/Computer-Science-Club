import java.util.*;

public class Contest_Feb_2021_SimonSays
{
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner(System.in);
      int n = kbd.nextInt();
      kbd.nextLine();
      
      String [] strings = new String[n];
      
      for (int i=0; i<n; i++)
      {
         strings[i] = kbd.nextLine();
      }
      
      for (int i=0; i<n; i++)
      {
         if (strings[i].length()<11)
            continue;
         else if (strings[i].substring(0,10).equals("Simon says"))
            System.out.println(strings[i].substring(11));
      }
   }
}