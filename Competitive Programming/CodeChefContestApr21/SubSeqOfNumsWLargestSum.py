'''
Specification
In this problem you are asked to write a program to find a contiguous 
subsequence of integers with the largest sum, within a given sequence of 
integer in list/array A (A has n integers). Formally, the task is to find 
indices i and j with 0 ≤ i ≤ j < n, such that the sum: 
A[i] + A[i+1] + … + A[j-1] + A[j] is as large as possible.

For example, for the list/array of values [−2, 1, −3, 4, −1, 2, 1, −5, 4], 
the contiguous subarray with the largest sum is [4, −1, 2, 1], with sum 6.

Input format
Each line has an integer.

Output format
The largest sum in a single line. If there are multiple subsequences with 
the same maximum sum, your program reports only one sum.
'''
nums = []
while True:
    try:
        inp = input()
    except EOFError:
        break
    if inp == "":
        break
    nums.append(int(inp))
max = 0
for num in nums:
    if num>max:
        max = num

for i in range(len(nums)):
    current = nums[i]
    for j in range(i+1, len(nums)):
        current += nums[j]
        if current>max:
            max = current
print(max)