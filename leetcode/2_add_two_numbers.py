# David Mas
# https://leetcode.com/problems/add-two-numbers/description/
# Medium
# Linked List, Math, Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()

        tmp = 0
        r = res
        while l1 or l2 or tmp > 0:
            val = 0

            if tmp == 1:
                val = 1
                tmp = 0

            if l1 is None and l2 is not None:
                val += l2.val
                l2 = l2.next
            elif l2 is None and l1 is not None:
                val += l1.val
                l1 = l1.next
            elif l2 is not None and l1 is not None:
                val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            
            if val > 9:
                val -= 10
                tmp = 1
            
            r.next = ListNode(val)
            r = r.next

        return res.next
