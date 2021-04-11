'''
Specification
Given a list of integers (one number per line), your program calculates 
the average of the numbers, excluding the max and min values (there is 
only one max value, and one min value). It is similar to judging the 
athlete's performance in gymnastics, in which the highest and the lowest 
scores are tossed out in the calculation of the average score.

Input format
Input consists at least three lines. Each line has an integer. There is 
only one maximum value, and one minimum value.

Output format
A floating-point number, rounded with 2 decimal places
'''

nums = []
max = 0.0
min = 0.0
while True:
    try:
        inp = input()
    except EOFError:
        break
    if inp == "":
        break
    num = float(inp)
    nums.append(num)
    if len(nums)==1:
        max = num
        min = num
    if num>max:
        max = num
    if num<min:
        min = num
filtered = []
for num in nums:
    if num < max and num > min:
        filtered.append(num)
# print(filtered)
avg = sum(filtered)/len(filtered)
print("{:0.2f}".format(avg))