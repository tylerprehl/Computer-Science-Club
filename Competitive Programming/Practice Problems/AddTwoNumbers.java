import java.util.*;
import java.math.BigInteger;

public class AddTwoNumbers
{
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner(System.in);
      
      LinkedList<Integer> l1 = new LinkedList<Integer>();
      LinkedList<Integer> l2 = new LinkedList<Integer>();
      
      String str1 = kbd.nextLine();
      String str2 = kbd.nextLine();
      
      for (int i = 0; i<str1.length(); i++)
         l1.add(Character.getNumericValue(str1.charAt(i)));
      
      for (int i = 0; i<str2.length(); i++)
         l2.add(Character.getNumericValue(str2.charAt(i)));
         
      LinkedList<Integer> sol = new LinkedList<Integer>();
      String solved = addTwoNumbers(l1,l2);
      System.out.print(solved);
      
      //for (int i = 0; i<sol.size(); i++)
        // System.out.print(sol.get(i));
   }
   public static String addTwoNumbers(LinkedList<Integer> l1, LinkedList<Integer> l2)
   {
      // more code
      String s1 = "";
      String s2 = "";
      
      for (int i = l1.size()-1; i>=0; i--) // get number 1 in correct order
         s1 += l1.get(i);
         
      for (int i = l2.size()-1; i>=0; i--) // get number 2 in correct order
         s2 += l2.get(i);
         
      BigInteger BI1 = new BigInteger(s1); // create Big Ints of Strings
      BigInteger BI2 = new BigInteger(s2);
      
      BI1 = BI1.add(BI2); // add Big Ints
      String answer = BI1.toString(); // convert sum back into String (has a decimal!)
      return answer;
   }
}