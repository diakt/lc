#141. Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/

# Not good. Used too much memory, feel like this would do better in long run/cautious veri but unsure
#Could have kicked into pointers early in array repeated distances
#after further examination of solutions, they assumed only one of each number would be provided, so 90% of this was purely vestigial
# 12 rt, 6 mem

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #if difference in pointers is the same then kick
        #12345345345345

        since = dict()
        
        if head == None or head.next == None:
            return False
        i=0
        while True:
            if head.val not in since:
                since[head.val] = [i, 0, 0]
            else:
                if (i-(since[head.val])[0]) == since[head.val][1]:
                    since[head.val][2] +=1
                    if since[head.val][2] > 3:
                        if since[head.next.val][2] == 3 or (head.val == head.next.val and since[head.next.val][2] == 4):
                            return i - (since[head.val][1]*since[head.val][2]*since[head.val][2])
                        else:
                            pass
                        
                else:
                    since[head.val][1] = (i-(since[head.val])[0])
            
            
            since[head.val][0] = i
            if head.next == None:
                break
            head=head.next
            i+=1

#yeah, so that got a little bit better
#53 rt 22 mem

class Solution(object):
    def hasCycle(self, head):
        

        since = set()
        
        if head == None or head.next == None:
            return False
        while True:
            if head in since:
                return True
            since.add(head)
            if head.next == None:
                return False
            head=head.next
            
        return False
        
#so we are beginning to recognize the value of slow/fast pointers
#80 rt, 63 mem

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
        