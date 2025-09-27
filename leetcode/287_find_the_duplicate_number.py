# David Mas
# https://leetcode.com/problems/find-the-duplicate-number/description/
# Medium
# Array, Two Pointers, Binary Search, Bit Manipulation

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ns = sorted(nums)

        for i in range(len(ns) - 1):
            if ns[i] == ns[i+1]:
                return ns[i]
