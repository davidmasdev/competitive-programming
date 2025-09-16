# David Mas
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Medium
# Array, Dynamic Programming, Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        seen = []

        for r in range(len(s)):
            if s[r] not in seen:
                seen.append(s[r])
                length = max(length, r - l + 1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.append(s[r])

        return length
