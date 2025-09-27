# David Mas
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Medium
# Hash Tablel, Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        relation = {}

        curr = head
        while curr:
            relation[curr] = Node(curr.val)
            curr = curr.next     

        curr = head
        while curr:
            relation[curr].next = relation.get(curr.next)
            relation[curr].random = relation.get(curr.random)
            curr = curr.next

        return relation[head]
