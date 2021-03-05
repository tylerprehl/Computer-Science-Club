'''
Search a Binary Search Tree for a given int "val". If val is in the tree, return true,
else return false.
'''

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, root, val):
        def search(self, root, val):
            if root == None:
                return False
            elif int(root.val) == val:
                return True
            elif int(root.val) < val:
                return search(self, root.right, val)
            elif int(root.val) > val:
                return search(self, root.left, val)
            return False
        return search(self,root,val)