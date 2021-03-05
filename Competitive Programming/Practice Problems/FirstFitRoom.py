'''
You are given a list of integers "rooms" and an integer "target". Return the first integer 
in rooms that's target or larger. If there is no solution, return -1.
'''

class Solution:
    def solve(self, rooms, target):
        for room in rooms:
            if room>=target:
                return room
        return -1