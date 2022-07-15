#100. Same Tree
# https://leetcode.com/problems/same-tree/

# First shot in around 8 min, not opt
# rt 82, mem 13

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # option 1: read one into hash table then check other
        # option 2: synchronous exploration
        # Note: based on val as well
        #could push into stack but would need to go in reverse order
        #I am weak on list representation of binary tree
        
        #four steps: check exists, check val, check roots
        
        #could start with hash table, read one in, then check another
        #lets start with that
        #will actually go with list
        

        def toList(node, tree):
            if node is None:
                tree.append(None)
            else:
                tree.append(node.val)
                toList(node.left, tree), toList(node.right, tree)
            return tree
        
        treep = toList(p, [])
        treeq = toList(q, [])
        print(treep, treeq)
        if treep == treeq:
            return True
        return False
        
            