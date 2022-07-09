# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

#copied off for understanding, more simple than could be imagined
#rt 72, mem 76

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #get length
        #point 5 to 1
        #set
        prev = None
        nxt = None
        current=head
        
        while current is not None: #while there are still new nodes to progress to
            nxt = current.next #next defined as head of 1, the 2
            current.next = prev #1 is pointed at the previous, which could be null (prev is not null after first, because we )

            prev = current # 1 is set as previous
            current = nxt #current is set as 2


        
        return prev

#rewrote for verification again, two steps
#rt and mem can be significantly effected by not defining nxt, though we need to define prev as it carries throughout
#honestly, tractable
#rt 86, mem 91

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        
        while current is not None:
            next = current.next
            current.next = prev
            
            prev = current
            current = next
        
        return prev
            

#after testing, we can see that perf is fairly stoch, there's not much to sharpen
            