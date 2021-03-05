import java.util.*;

public class Contest_Feb_2021_FlexibleSpaces
{
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner(System.in);
      String line1 = kbd.nextLine();
      String line2 = kbd.nextLine();
      
      String [] line1split = line1.split(" ");
      
      int length = Integer.valueOf(line1split[0]);
      int parts = Integer.valueOf(line1split[1]);
      
      String [] line2split = line2.split(" ");
      int [] partPoints = new int[line2split.length];
         
      for (int i=0; i<partPoints.length; i++)
         partPoints[i] = Integer.valueOf(line2split[i]);
      
      int [] points = new int[parts+2];
      points[0] = length;
      points[points.length-1] = 0;
      
      int index = partPoints.length-1;
      for (int i = 1; i<points.length-1; i++)
      {
         points[i] = partPoints[index];
         index--;
      }
      
      ArrayList<Integer> differences = new ArrayList<Integer>();
      for (int i = 0; i<points.length; i++)
      {
         for (int j = i+1; j<points.length; j++)
         {
            if (differences.indexOf(points[i]-points[j])==-1)
               differences.add(points[i]-points[j]);
         }
      }
      Collections.sort(differences);
      for (int i = 0; i<differences.size(); i++)
         System.out.println(differences.get(i));      
   }
}