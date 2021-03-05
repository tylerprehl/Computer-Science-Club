import java.util.*;

public class BrickWallPatterns
{
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner(System.in);
      
      // Uses Binet's Theorem to find the nth value of the Fibonacci Sequence
      boolean end = true;
      double Phi = (Math.sqrt(5)+1)/2;
      double phi = (Math.sqrt(5)-1)/2;
      
      while (end)
      {
         int n = kbd.nextInt();
         int fibN = n+1;
         if (n==0)
         {
            end = false;
         }
         else
         {
            double answer = (Math.pow(Phi,fibN)-Math.pow(phi,fibN))/Math.sqrt(5);
            System.out.println(Math.round(answer));
         }
      }
   }
}