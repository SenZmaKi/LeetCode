# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxes: list[float] = [-float("inf")] * len(prices)
        for index, price in reversed(list(enumerate(prices))):
            if index == len(maxes) - 1:
                maxes[index] = price
            elif price > maxes[index + 1]:
                maxes[index] = price
            else:
                maxes[index] = maxes[index + 1]
        max_profit = 0
        for index, price in enumerate(prices[:-1]):
            profit = maxes[index + 1] - price
            if profit > max_profit:
                max_profit = profit
        return int(max_profit)

    # Kadane's Algorithm
    def maxProfitCorrect(self, prices: list[int]) -> int:
        if not prices:
            return 0
        maxProfit = 0
        buyPrice = prices[0]
        for price in prices[1:]:
            # Using if statements seems to be much faster in Python tho
            # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1663792059/
            # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1663792221/
            buyPrice = min(price, buyPrice)
            maxProfit = max(maxProfit, price - buyPrice)
        return maxProfit


sol = Solution()
prices = [3, 10, 1]
result = sol.maxProfitCorrect(prices)
print(result)
