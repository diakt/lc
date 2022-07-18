# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Wow. Two hours before you realize a BST is not a BT. Social science issues. Got it in one shot after.
# Anki.
# 75 rt, 25 mem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            pass
        if (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val) or (root.val == p.val) or (root.val == q.val):
            return root
        elif (root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
            
        elif (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
                
    
    
    
  
            
                
            
            
        