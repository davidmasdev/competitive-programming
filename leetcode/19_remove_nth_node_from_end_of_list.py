# David Mas
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Medium
# Linked List, Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1

        i = l - n + 1
        if i == 1:
            return head.next

        c = head
        while c:
            if i-2 <= 0:
                break
            c = c.next
            i -= 1
            
        if not c.next: return None
        c.next = c.next.next

        return head
