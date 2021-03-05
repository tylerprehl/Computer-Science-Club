import java.util.*;

/*
   Eight Queens:
   If 8 Queens (asterisks) are on the 8x8 board (rest of spaces are periods) such that
   none are threatening each other, print "valid," else, print "invalid."
   
   Strategy:
   Create 8x8 board as 2D array
   Get points of queens (x,y in array)
   Check if any queens have same x (horizontal)
   Check if any queens have same y (vertical)
   Check if any queens have slope of 1 or -1 (diagonals)
   If all checks return true, print valid
   
   Update: success!
*/

public class Contest_Feb_2021_EightQueens
{   
   public static void main(String[] args) 
   {
       char [][] board = new char[8][8];
       board = getBoard(board);
       int [][] queens = new int[8][2];
       queens = getQueens(board, queens);
       if (queenCheck(queens)) 
           System.out.println("valid");
       else 
           System.out.println("invalid");
   }
      
   static boolean horizontalCheck(int[][] queens)
   {
      for (int i = 0; i<8; i++)
      {
         for (int j = i+1; j<8; j++)
         {
            if (queens[i][0]==queens[j][0])
            {
               System.out.println("Failed horizontal check");
               System.out.println("Queen 1: "+i+"\nQueen 2: "+j); // which queens
               System.out.println(queens[i][0]+" "+queens[i][1]+"\n"+
                                  queens[j][0]+" "+queens[j][1]);
               return false;
            }
         }
      }
      return true;
   }
   static boolean verticalCheck(int[][] queens)
   {
      for (int i = 0; i<8; i++)
      {
         for (int j = i+1; j<8; j++)
         {
            if (queens[i][1]==queens[j][1])
            {
               System.out.println("Failed vertical check");
               System.out.println("Queen 1: "+i+"\nQueen 2: "+j); // which queens
               System.out.println(queens[i][0]+" "+queens[i][1]+"\n"+
                                  queens[j][0]+" "+queens[j][1]);
               return false;
            }
         }
      }
      return true;
   }
   static boolean diagonalCheck(int[][] queens)
   {
      for (int i = 0; i<8; i++)
      {
         for (int j = i+1; j<8; j++)
         {
            double slope = ((double)queens[j][1]-(double)queens[i][1])/((double)queens[j][0]-(double)queens[i][0]);
            
            if (slope == 1 || slope == -1)
            {
               System.out.println("Failed diagonal check");
               System.out.println("Queen 1: "+i+"\nQueen 2: "+j); // which queens
               System.out.println(queens[i][0]+" "+queens[i][1]+"\n"+
                                  queens[j][0]+" "+queens[j][1]);
               return false;
            }
         }
      }
      return true;
   }
   
   static boolean queenCheck(int[][] queens)
   {
      boolean horizontal = horizontalCheck(queens);
      boolean vertical = verticalCheck(queens);
      boolean diagonal = diagonalCheck(queens);
      if (horizontal && vertical && diagonal)
         return true;
      else
         return false;
   }
   
   static int[][] getQueens(char[][] board, int[][] queens)
   {
      int queenI = 0;
      for (int i = 0; i<8; i++)
      {
         for (int j = 0; j<8; j++)
         {
            if (board[i][j]=='*')
            {
               queens[queenI][0] = i;
               queens[queenI][1] = j;
               queenI++;
            }
         }
      }
      for (int i = 0; i<8; i++)
         System.out.println("Queen "+i+": "+queens[i][0]+" "+queens[i][1]);
      return queens;
   }
   
   static char[][] getBoard(char[][] board)
   {
      Scanner kbd = new Scanner(System.in);
      
      for (int i = 0; i<8; i++)
      {
         String input = kbd.nextLine();
         String [] split = input.split(" ");
         for (int j = 0; j<8; j++)
         {
            board[i][j] = split[j].charAt(0);;
         }
      }
      return board;
   }
}
/*
Tests:
valid test
. . . . . * . .
* . . . . . . .
. . . . * . . .
. * . . . . . .
. . . . . . . *
. . * . . . . .
. . . . . . * .
. . . * . . . .

invalid (fail vertical)
. . . . . . . *
. . . * . . . .
. . . . . . * .
. . * . . . . .
. . . . . * . .
. * . . . . . .
. . . . * . . .
. . . . * . . .

invalid (fail horizontal)
* . . . . . . *
. . . * . . . .
. . . . . . * .
. . * . . . . .
. . . . . * . .
. * . . . . . .
. . . . * . . .
. . . . . . . .

invalid (fail diagonal)
. . . . . . . *
. . . * . . . .
. . . . . . * .
. . * . . . . .
. * . . . . . .
. . . . . * . .
. . . . * . . .
* . . . . . . .
*/