class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            temp = max(profit, prices[i] - minimum)

            minimum = min(minimum, prices[i])

            profit = temp
        
        return profit
