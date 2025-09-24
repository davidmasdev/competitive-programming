# David Mas
# https://leetcode.com/problems/linked-list-cycle/description/
# Easy
# Hash Table, Linked List, Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = []

        while head:
            if head.next in stack:
                return True
            stack.append(head)
            head = head.next
        
        return False
