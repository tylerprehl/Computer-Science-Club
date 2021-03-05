import java.util.*;

/*
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
The objective of the puzzle is to move the entire stack to another rod, 
obeying the following simple rules: 

1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing 
it on top of another stack (i.e. a disk can only be moved if it is the uppermost 
disk on a stack.)
3) No disk may be placed on top of a smaller disk.

*/

public class TowerOfHanoi
{
   public static void main(String[]args)
   {
      Scanner kbd = new Scanner(System.in);
      System.out.println("How many disks would you like? ");
      int n = kbd.nextInt();
      System.out.println("The following are the steps to solve the Tower of Hanoi with "
                           +n+" disks.");
      tower(n, 'A', 'C', 'B');
      System.out.println("Completed.");
   }
   
   public static void tower(int n, char from, char to, char aux)
   {
      if (n==1) {
         System.out.println("Move "+n+" from "+from+" to "+to);
         return;
      }
      tower(n-1, from, aux, to); // gets all plates above bottom plate onto B
      System.out.println("Move "+n+" from "+from+" to "+to); // moves bottom plate from A to C
      tower(n-1, aux, to, from); // gets all plates from B onto C
   }
}