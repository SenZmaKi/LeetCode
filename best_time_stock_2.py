# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    # Greedy Algorithm
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]
        return profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
res = sol.maxProfit(prices)
print(res)
