# 21. Merge Two Storted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

#difficult. Not as familiar with linked lists as I thought
#term conditions are iffy, creating a node and a poiner to it, saving a first node as a new head
# 64 rt, 58 mem
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        
        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
                
            if list1.val <= list2.val:
                tail.next = list1
                list1=list1.next
            else:
                tail.next = list2
                list2=list2.next
            
            tail=tail.next
            
            
        return dummy.next
            
