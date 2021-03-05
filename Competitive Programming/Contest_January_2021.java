import java.util.*;

public class Contest_January_2021
{
   /*
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner (System.in);
      int n = kbd.nextInt();
      kbd.nextLine();
      
      for (int i = 0; i < n; i ++) 
      {
         String str = kbd.nextLine();
         String [] delimiter = str.split(" ");
         
         String statement = kbd.nextLine() + " ";
         
         if(delimiterCheck(delimiter[0], delimiter[1], statement))
            System.out.println(statement+"is balanced");
         else
            System.out.println(statement+"is not balanced");
      }
   }
   
   public static boolean delimiterCheck(String s1, String s2, String s)
   {
      Stack<String> stk= new Stack<String>();
      if (s==null||s.length()==0)
         return true;
      for (int i=0; i<s.length()-s2.length()+1; i++)
      {
         if (s.substring(i,i+s2.length()).equals(s2))
         {
            if (stk.isEmpty())
               return false;
            if (stk.peek().equals(s1))
            {
               stk.pop();
               i++;
            }
         }
         if (s.substring(i,i+s1.length()).equals(s1))
            stk.push(s1);
      }
      if (stk.isEmpty())
         return true;
      else
         return false;
   }
   */
   
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner (System.in);
      int n = kbd.nextInt();
      kbd.nextLine();
      
      for (int i=0; i<n; i++)
      {
         String str = kbd.nextLine();
         String [] nums = str.split(" ");
         int n1 = Integer.parseInt(nums[0]);
         int n2 = Integer.parseInt(nums[1]);
         int n3 = Integer.parseInt(nums[2]);
         
         System.out.println(getCombos(n1, n2, n3));
      }
   }
   
   public static int getCombos(int digits, int start, int last)
   {
      int count = 0;
      int [] current = new int[digits];
      int [] lastNum = new int[digits];
      int [] holder = new int[digits];
      int stopper = 1;
      
      for (int i = 0; i<digits; i++)
      {
         current[i] = start;
         holder[i] = start;
         lastNum[i] = last;
      }
      
      for (int j=0; j<digits; j++)
      {
         while(current[j]<last)
         {
            for (int i = digits-1; i>=0; i--)
            {
               current[i]++;
               count++;
            }
         }
         for (int i = 0; i<digits; i++)
            current[i] = holder[i];
         current[digits-stopper]++;
         stopper++;
      }
      return count;
   }
}