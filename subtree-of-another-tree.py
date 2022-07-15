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
        
#took another shot at it
#who could have known, defining a function within a recursive function takes memory
# how did I graduate
# ~60 rt, ~40 mem    

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
    
        if not subRoot:
            return True
        
        elif not root:
            return False
            
        elif root and subRoot:
            if self.isSame(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
            
    
    
    def isSame(self, root, subRoot):
        
        if root is None and subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        if root is not None and subRoot is None:
            return False
        else:
            if root.val == subRoot.val:
                return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
            else:
                return False
            
        