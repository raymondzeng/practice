# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        
        temp = ListNode(-1)
        temp.next = head
        
        curr = 0
        before_m = None
        before_n = None
        hold_m = None
        hold_n = None
        while(temp != None):
            if curr + 1 == m:
                before_m = temp
                hold_m = temp.next
            if curr + 1 == n:
                before_n = temp
                hold_n = temp.next
                break
            
            curr += 1
            temp = temp.next
            
        before_m.next, hold_n.next, before_n.next, hold_m.next = hold_n, hold_m.next, hold_m, hold_n.next
        
        return head
