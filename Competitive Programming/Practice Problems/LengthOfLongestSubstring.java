import java.util.*;

class LengthOfLongestSubstring {
    public static void main(String[]args)
    {
      System.out.println(lengthOfLongestSubstring("abcabcbb")); // expects 3
      System.out.println(lengthOfLongestSubstring("pwwkew")); // expects 3
      System.out.println(lengthOfLongestSubstring("dvdf")); // expects 3
      System.out.println(lengthOfLongestSubstring("aabaab!bb")); // expects 3
    }
    
    public static int lengthOfLongestSubstring(String s) 
    {
      LinkedList<String> chars = new LinkedList<String>();
      ArrayList<Integer> counts = new ArrayList<Integer>();
      int count = 0;
      
      for (int i = 0; i<s.length(); i++)
      {
         if (chars.indexOf(s.substring(i,i+1))==-1)
         {
            chars.add(s.substring(i,i+1));
            count++;
         }
         else
         {
            counts.add(count);
            
            boolean unremoved = true;
            while (unremoved)
            {
               if (chars.getFirst().equals(s.substring(i,i+1)))
               {
                  chars.removeFirst();
                  chars.add(s.substring(i,i+1));
                  unremoved = false;
               }
               else
                  chars.removeFirst();
            }
            count = chars.size();
         }
      }
      
      for (int i = 0; i<counts.size(); i++)
      {
         if (counts.get(i)>count)
            count = counts.get(i);
      }
      return count;
    }
}