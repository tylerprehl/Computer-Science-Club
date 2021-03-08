
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


Need:
list of weights (sorted ints)
runningSum:
    - self-explanatory
savedSum:
    - for comparison against runningSum

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
initial = input().split()
n = int(initial[0])
maxCap = int(initial[1])
weights = []
for i in range(n):
    weights.append(int(input()))
weights.sort()

currentTotal = weights[0]
if currentTotal == maxCap:
    print(maxCap)
    exit()
runningSum = weights[0]
savedCap = 0
best = maxCap
for i in range(1,n): # loop through all (sorted) given weights
    if weights[i]==weights[i-1]: # if multiple weights are the same, need to skip to next different number when we reach capacity with the same numbers. If it reaches end of list, just prints what the last runningSum was that was under maxCap
        if runningSum+weights[i]<=maxCap: 
            runningSum+=weights[i]
        else:
            best = runningSum
    elif weights[i]<runningSum: # see if you can lessen lowest capacity with a larger number (21, 50, 70, cap 80)
        savedSum = runningSum # want to hold on to previous runningSum in case it doesn't work out
        runningSum = weights[i]
        for j in range(i): # add weights back into runningSum from smallest to greatest, going to else if the next number exceeds capacity
            if runningSum+weights[j]<=maxCap: 
                runningSum+=weights[j] # if all j's are just added back in, we go back to original loop and forget this ever happened
            else: # since savedSum represents a point in time 
                if savedSum<runningSum:
                    if savedSum+weights[i]<=maxCap:
                        runningSum = savedSum+weights[i] # nothing came of this, so just add
                    else:
                        if savedSum<best:
                            best = savedSum
                else:
                    if runningSum<best:
                        best = runningSum
    else: # if next num is equal to or less than runningSum...
        if runningSum+weights[i]<=maxCap:
            runningSum+=weights[i]
        else:
            if runningSum<best:
                best = runningSum
print(best) # prints what's left in best when loop ends 

