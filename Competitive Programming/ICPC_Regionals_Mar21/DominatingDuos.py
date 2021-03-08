
'''
A group of people are standing in a line. Each person has a distinct 
height. You would like to count the number of unordered pairs of people 
in the line such that they are taller than everyone in between them in 
the line.

More formally, let d be a sequence of the heights of the people in order 
from left to right. We want to count the number of pairs of indices i and 
j with i<j such that for all k with i<k<j, di>dk and dj>dk. Note that if 
j=i+1 (i.e., there are no k’s between i and j), it is trivially true.

Input:
The first line of input contains an integer n (2≤n≤106), which is the 
number of people.

Each of the next n lines contains a single integer di (1≤di≤n). These are 
the heights of the people in the group, in the order in which they’re 
standing. The sequence is guaranteed to be a permutation of the integers 
1 through n.

Output:
Output a single integer, which is the number of pairs of people who are 
taller than everyone between them.


To solve:
int pairs - count of pairs that pass the height check 
    1) add length of list minus 1 to pairs (accounts for all pairs
       directly next to each other)
    2) loop through list such that you check if for x heights over (x>1), 
       the heights in between are less than heights on either side
       - if a pair passes check, add 1 to pairs

'''