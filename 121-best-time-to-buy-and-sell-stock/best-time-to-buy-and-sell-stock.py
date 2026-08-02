class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                # Found a cheaper buying price
                buy = sell

            sell += 1

        return max_profit