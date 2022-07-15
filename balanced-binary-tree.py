# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree

# Ouch. Need to come back to this. Didn't figure out passing an array, wrote two functions, essentially swung around the solution doing 95% right
#think could be done with a height function but this was painful
# 39 rt, 36 mem

## Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        
        def dfs(root):
            
            if root is None:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] == True and right[0] == True and abs(left[1]-right[1]) < 2)
            
            return [balanced, 1+max(left[1],right[1])]
        
        dingo = dfs(root)
        
        return dingo[0]

#later shot, some variability but quick learning pattern
#feel could maybe play around with rem left, right def for mem but unsure how to call once and check conditions based on both arr 0, 1 at same time w/o calling twice
# 60 rt, 36 mem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        def dfs(node):
            if node is None:
                return [True, 0]
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                balanced = (left[0] and right[0] and abs(left[1]-right[1])<2)
                return [balanced, max(left[1],right[1])+1]
            
        return dfs(root)[0]
       
        
                
        
        