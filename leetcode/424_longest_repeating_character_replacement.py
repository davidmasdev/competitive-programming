# David Mas
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Medium
# Hash Table, String, Sliding Window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1

            if r - l + 1 - max(freq.values()) <= k:
                length = max(r - l + 1, length)
            else:
                freq[s[l]] -= 1
                l += 1

        return length

