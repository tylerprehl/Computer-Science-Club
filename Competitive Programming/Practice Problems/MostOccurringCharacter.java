import java.util.*;

/*
Problem posed by Vanguard:
Given a random string of characters, determine which character occurs the most in the 
string and return how many times it appears
*/

public class MostOccurringCharacter
{
   public static void main(String[]args)
   {
      String chars = "abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*();',./ ";
      String randStr = "";
      Random rand = new Random();
      for (int i = 0; i<1000; i++) {
         randStr += chars.charAt(rand.nextInt(78)); // 128 accounts for all possible ASCII characters
      }
      String test1 = "aqoddrpwuddcxndiefnejkleowifjldddlaljelddddkjelfh;dlsfddjldskfj5555555555555555"; // 16 d's and 16 5's, should give 
      String test2 = "hello world, letters like l are awfully long silly?"; // 11 L's
      
      int testNum1 = getMOC(test1); //should be 16 d's
      System.out.println("Occurances: " + testNum1);
      int testNum2 = getMOC(test2);
      System.out.println("Occurances: " + testNum2);
      int testNum3 = getMOC(test3);
      System.out.println("Occurances: " + randStr);
   }
   
   static int getMOC(String text)
   {
      /* Hash Map Idea: (success!)
      As loop progresses, store each character in key of hash map
      As loop progresses, store/update # of character appearances in definition of hash map
      Simultaneously, store most occuring character and # of appearances in char and int
      After loop completes, display most occurring char and return # of appearances
      */
      char moc = text.charAt(0);
      int bestCount = 1;
      
      HashMap<Character, Integer> chars = new HashMap<Character, Integer>(128); 
      chars.put(text.charAt(0), 1);
      
      char currentMOC = text.charAt(0);
      
      for (int i = 1; i<text.length(); i++)
      {
         if (!chars.containsKey(text.charAt(i)))
            chars.put(text.charAt(i), 1);
         else
         {
            chars.replace(text.charAt(i), chars.get(text.charAt(i))+1);
            if (chars.get(text.charAt(i))>bestCount)
            {
               bestCount = chars.get(text.charAt(i));
               moc = text.charAt(i);
            }
         }
      }
      System.out.println(chars.toString());
      
      System.out.print("Most occurring character: "+moc+"  ");
      return bestCount;
   }
}