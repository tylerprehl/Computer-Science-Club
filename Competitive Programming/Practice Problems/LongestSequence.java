import java.util.*;

/*
This was a problem posed by Vanguard:
Given a list of integers, return the number of ints in the longest sequence such that
the next integer (j) is either also j or j+1.
*/

public class LongestSequence
{
   public static void main(String[]args)
   {
      List<Integer> list = new ArrayList<Integer>(100);
      Random rand = new Random();
      for (int i = 0; i<100; i++) {
         list.add(rand.nextInt(101));
      }
      System.out.println("Original list: "+list);
      System.out.println(getLongestSequence(list));

   }
   
   static int getLongestSequence(List<Integer> list)
   {
      LinkedList<Integer> longestSequence = new LinkedList<Integer>();
      int longestCount = 1;
      LinkedList<Integer> currentSequence = new LinkedList<Integer>();
      int currentCount = 1;
      
      Collections.sort(list);
      
      currentSequence.add(list.get(0));
      for (int i = 1; i<list.size(); i++)
      {
         if (list.get(i)==list.get(i-1) || list.get(i)==list.get(i-1)+1)
         {
            currentCount++;
            currentSequence.add(list.get(i));
         }
         else
         {
            if (currentCount>longestCount)
            {
               longestSequence.clear();
               for (int j = 0; j<currentSequence.size(); j++)
                  longestSequence.add(currentSequence.get(j));
               longestCount = currentCount;
               currentCount = 1;
               currentSequence.clear();
               currentSequence.add(list.get(i));
            }
            else
            {
               currentCount = 1;
               currentSequence.clear();
               currentSequence.add(list.get(i));
            }
         }
      }
      
      System.out.print("Sorted list: "+list+"\nLongest sequence: "+
                        longestSequence+"\nSequence count: ");
      return longestCount;
   }
}