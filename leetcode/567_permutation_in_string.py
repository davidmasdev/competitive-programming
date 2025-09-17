# David Mas
# https://leetcode.com/problems/permutation-in-string/description/
# Medium
# Hash Table, Two Pointers, String, Sliding Window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}

        for i in range(len(s2)):
            if s2[i] in seen:
                seen[s2[i]] -= 1
            if i >= len(s1) and s2[i-len(s1)] in seen:
                seen[s2[i-len(s1)]] += 1
            if all([seen[i] == 0 for i in seen]):
                return True
        return False
