import java.util.*;

public class ExponentialTowers
{
   public static void main(String[]args)
   {
      int x = 2;
      int y = 2;
      int z = 2;
      int count = 0;
      
      Scanner kbd = new Scanner(System.in);      
      int a = kbd.nextInt();
      int b = kbd.nextInt();
      int c = kbd.nextInt();
      
      double n = Math.pow(a,b*c);
      
      while (x<=Math.sqrt(Math.sqrt(n)))
      {
         while (y<50)
         {
            while (z<50)
            {
               if (Math.pow(x,Math.pow(y,z))==n)
               {
                  System.out.println(x+"  "+y+"  "+z);
                  count++;
               }
               z++;
            }
         z=2;
         y++;
         }
      y=2;
      z=2;
      x++;
      }
      System.out.println("There are "+(count)+" ways.");
   }
}