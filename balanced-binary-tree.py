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

        
        
        