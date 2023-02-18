class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            elif prices[i] - minBuy > maxProfit:
                maxProfit = prices[i] - minBuy
        return maxProfit
        