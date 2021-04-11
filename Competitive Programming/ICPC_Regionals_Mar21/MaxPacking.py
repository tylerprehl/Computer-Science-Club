
'''
We have a knapsack of integral capacity and some objects of assorted 
integral sizes. We attempt to fill the knapsack up, but unfortunately, 
we are really bad at it, so we end up wasting a lot of space that can’t 
be further filled by any of the remaining objects. In fact, we are 
optimally bad at this! How bad can we possibly be?

Figure out the least capacity we can use where we cannot place any of 
the remaining objects in the knapsack. For example, suppose we have 3 
objects with weights 3, 5 and 3, and our knapsack has capacity 6. If we 
foolishly pack the object with weight 5 first, we cannot place either of 
the other two objects in the knapsack. That’s the worst we can do, so 5 
is the answer.

Input
The first line of input contains two integers n (1≤n≤1000) and c 
(1≤c≤105), where n is the number of objects we want to pack and c is the 
capacity of the knapsack.

*****************************
Max's work

n = number of objects
c = capacity
w = weight of AN object

L = list of object weights

K = list of object weights in bag

ans = sum(K) where max(c - sum(K))

ans = min sum(K)

Assumptions

sum(L) > c



********************************

Each of the next n lines contains a single integer w (1≤w≤c). These are 
the weights of the objects.

Output
Output a single integer, which is the least capacity we can use where we 
cannot place any of the remaining objects in the knapsack.

Trials
cap 100 (unless otherwise specified)
50, 51 - least is 50
25, 50, 51 - least is 75 <- 50>sum of previous, but can add 25
25, 27, 50, 51 - least is 52 (uses 25 & 27)
40, 50, 70 - least is 70 (with 49, can put in 50) <- 70<sum of previous && nothing previous can be added
21, 50, 70 (cap 80) - least is 70 (70<runningSum)
20, 50, 70 - least is 70 (70==runningSum, no need for runningSum sequence)
10, 25, 60, 61
3, 3, 3, 3, 5 (cap 10)
3, 3, 5 (cap 6)
2, 3, 3, 5 (cap 6)

Solve Method:
1) Get weights into sorted list (check)
2) set runningsum=1st weight
    if runningSum=maxCap, minCap=maxCap
3) Then must check for all weights:
is this number the same as the last number?
    - if so:
        if you CAN add it and be under capacity:
            - add it, if it's the last number in the list, print runningSum
        if you canNOT add it, if it's the last number, print runningSum

is runningSum>current number?
    - if so:
        save current capacity (savedCap)
        runningSum=current number, add previous numbers until either:
            - next number won't fit in capacity (found possible answer)           
            - back to current number in list (go to next number)
        
    - if not, can you add current number without going over capacity?
        - if yes, do so, go to next num in list
            if last number, add to list, total sum is minimum cap
        - if no, found possible answer 

'''
import itertools
from typing import List

tests = [
    (100, [50, 51], 50),
    (100, [25, 50, 51], 75),
    (100, [25, 27, 50, 51], 52),
    (100, [40, 50, 70], 70),
    (80, [21, 50, 70], 70),
    (100, [20, 50, 70], 70),
    (100, [10, 25, 60, 61], 95),
    (100, [15, 25, 60, 61], 76),
    (10, [3, 3, 3, 3, 5], 8),
    (6, [3, 3, 5], 5),
    (6, [2, 3, 3, 5], 5),
    (100, [15,15,15,15,15,16,18,70,90], 86)
]

def maxpack(cap, weights: List[int]):
    # print("\n", weights)
    best = cap + 1
    # every list of different lengths
    for i in range(len(weights)):
        # every combination within that length
        for boyo in itertools.combinations(weights, i+1):
            rest = weights.copy()
            bruh = sum(boyo)
            for nib in boyo:
                rest.remove(nib)

            # print(bruh, "\t", boyo, rest)
            
            if bruh > cap:
                # print("bruh > cap")
                continue
            # get rid of combos where a number can be added and still be less than cap
            if len(rest) > 0 and rest[0] + bruh <= cap:
                # print("bruh + rest still < cap")
                continue
            if bruh < best:
                best = bruh
                # print("new best")
                continue
            # print ("best was better")
    return best

def test():
    for test in tests:
        print(maxpack(test[0], test[1]), "\t", test[2], "\tlist=", test[1])

if __name__ == "__main__":
    initial = input().split()
    n = int(initial[0])
    maxCap = int(initial[1])
    weights = []
    for i in range(n):
        weights.append(int(input()))
    weights.sort()
    maxpack(maxCap, weights)
    # test()
