'''
Specification
In this problem you are asked to write a program to determine if two words 
come from the same base alphabet. When one word is a rearrangement of 
letters of the other, the two words are called “anagrams”, like “rose” and 
“sore”. But this problem asks you to determine if two words use the same 
letters, not necessarily use equal numbers of them. For example, “curse” 
and “rescue” come from the same base alphabet, but “cure” does not, since 
its base alphabet does not contain the “s” that both “curse” and “rescue” 
use.

Input Format
The input consists of multiple lines, each line with a pair of words 
separated by spaces. The words have only lowercase letters.

Output:
Output Yes or No for each line of input.
'''
while True:
    try:
        inp = input()
    except EOFError:
        break
    if inp == "":
        break
    splitInp = inp.split()
    words = []
    for word in splitInp:
        letters = set()
        for letter in word:
            letters.add(letter)
        words.append(letters)
            
    # print(words)
    if words[0] == words[1]:
        print("Yes")
    else:
        print("No")