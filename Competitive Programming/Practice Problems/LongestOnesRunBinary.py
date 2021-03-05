'''
Find the longest string of 1's in a binary number given integer "n"
'''

class Solution:
    def solve(self, n):
        best = 0
        current = 0
        binary = bin(n)[2:]

        for digit in map(int, binary):
            if digit == 1:
                current += 1
                if current>best:
                    best=current

            if digit == 0:
                if current > best:
                    best = current
                    current = 0
                current=0

        return best