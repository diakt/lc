# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree

#Pretty happy with this, came quickly
#68 rt, 74 mem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            pass
        elif root.left is None and root.right is None:
            return root

        elif root.left is None:
            root.left = self.invertTree(root.right)
            root.right = None

        elif root.right is None:
            root.right = self.invertTree(root.left)
            root.left = None

        else: 
            dummyTrans = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(dummyTrans)

        return root
            
       
            
            
            #flop, and keep flopping down
            