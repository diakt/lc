# 104. Maximum depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree

#Not quite sure what is making this so slow, probably null handling
#or max, to be honest
#5 rt, 54 mem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.maxDepth(root.right) +1
        elif root.right is None:
            return self.maxDepth(root.left) +1
        elif root.left is not None and root.right is not None:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        
 #Aha. It was second condition.
 # rt 50, mem 34

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0


        elif root.left is None:
            return self.maxDepth(root.right) +1
        elif root.right is None:
            return self.maxDepth(root.left) +1
        elif root.left is not None and root.right is not None:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        
        
        
        
        
        
        
        