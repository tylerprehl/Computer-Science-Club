import java.util.*;

public class MorseCodeDecoder
{
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner (System.in);
      
      String [][] alphabet = new String[36][2];
      
      for (int i = 0; i<36; i++)
      {
         String str = kbd.nextLine();
         String [] split = str.split(" ",0);
         alphabet[i][0] = split[0];
         alphabet[i][1] = split[1];
      }
      
      int n = kbd.nextInt();
      kbd.nextLine();
      String [] lines = new String[n];
      
      for (int i = 0; i<n; i++)
      {
         String str = kbd.nextLine();
         String decodedStr = "";
         
         String [] codeLtr = str.split("   ",0);
      
         for (int k = 0; k<codeLtr.length; k++)
         {
            for (int j = 0; j<alphabet.length; j++)
            {
               if (alphabet[j][1].equals(codeLtr[k]))
               {
                  decodedStr+=alphabet[j][0];
                  break;
               }
            }
         }
         lines[i] = decodedStr;
      }
      
      for (int i = 0; i<n; i++)
      {
         System.out.println(lines[i]);
      }
   }
}