# David Mas
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Easy
# Array, Dynamic Programming, Sliding Window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        l = 0
        r = 0
        for r in range(len(prices)):
            diff = max(diff, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r

        return diff
