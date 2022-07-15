#572. Subtree of another tree
#https://leetcode.com/problems/subtree-of-another-tree/

#Around 40 minutes. Pretty ugly. Anti-pattern with double recursion, high mem, and multi-condition parsing
#Still hit though
#37 rt, 12 mem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        def subroot(root, pattern):
            if root is None and pattern is None:
                return True
            elif root is not None and pattern is None:
                return False
            elif root is None and pattern is not None:
                return False
            else:
                if root.val == pattern.val:
                    return (subroot(root.left, pattern.left) and subroot(root.right, pattern.right))
                else: 
                    return False
                
        found = False
        if root is not None :
                if root.val == subRoot.val:
                    found = True
                    if subroot(root, subRoot) is False:
                        found = False
                        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
                    else:
                        return True
                else: 
                    return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        elif root is None :
            pass
        
        print("here")
        return found
        
            
            