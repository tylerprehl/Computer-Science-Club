'''
You are teaching kindergarten! You wrote down the numbers from 1 to n, 
in order, on a whiteboard. When you weren’t paying attention, one of your 
students erased one of the numbers. Can you tell which number your 
mischievous student erased?

Input
The first line of input contains a single integer n (2≤n≤100), which is 
the number of numbers that you wrote down.

The second line of input contains a string of digits, which represents 
the numbers you wrote down (minus the one that has been erased). There 
are no spaces in this string. It is guaranteed to contain all of the numbers 
from 1 to n, in order, except for the single number that the student erased.

Output
Output a single integer, which is the number that the tricky student erased.
'''

numbers = input()
sizeNum = len(numbers)
num = int(numbers)

givenList = input()
ourList = "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100"

if givenList[-sizeNum:]==numbers:
    # when the number of digits changes, change the number of characters compared
    if num<10: # if biggest number is <=9
        for j in range(num):
            if givenList[j:j+1]!=ourList[j:j+1]:
                print(ourList[j:j+1])
                exit()
               
    elif num<=100: # if biggest number is 100
        for j in range(10):
            if givenList[j:j+1]!=ourList[j:j+1]:
                print(ourList[j:j+1])
                exit()
        for j in range(10,len(givenList),2):
            if givenList[j-1:j+1]!=ourList[j-1:j+1]:
                print(ourList[j-1:j+1])
                exit()
else:
    print(num)
