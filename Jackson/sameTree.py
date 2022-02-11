# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""Looked at a hint"""
class Solution(object):
    def isSameTree(self, p, q):
        return self.recurse(p,q)
        
    def recurse(self, p, q):
        """If both nodes do not exist"""
        if not p and not q:
            return True 
        """If one node exists and the other does not"""
        if not p or not q:
            return False
        """If their values are not equal"""
        if p.val != q.val:
            return False      
        """Recurse through the tree, and return true if it was able to get to bottom
        without values being unequal. If both sides true, return true. Else, return false."""
        if self.recurse(p.left, q.left) and self.recurse(p.right, q.right) == True:
            return True
        else:
            return False
