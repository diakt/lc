#asdf. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/submissions/

#Ugly one. Toughed it out
# 12 rt, 42 mem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def height(self, root):
        if root.left is None and root.right is None:
            return 0
        elif root.left is None and root.right is not None:
            return self.height(root.right)+1
        elif root.left is not None and root.right is None:
            return self.height(root.left)+1
        elif root.left is not None and root.right is not None:
            return max(self.height(root.left), self.height(root.right))+1
    
    def diameterOfBinaryTree(self, root):
        if root.left is None and root.right is None:
            return 0
        
        elif root.left is not None and root.right is None:
            return max(self.height(root.left)+1,self.diameterOfBinaryTree(root.left))
        elif root.left is None and root.right is not None:
            return max(self.height(root.right)+1,self.diameterOfBinaryTree(root.right))
        
        elif root.left is not None and root.right is not None:
            return max(max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)), self.height(root.left)+self.height(root.right)+2)
        
        

        