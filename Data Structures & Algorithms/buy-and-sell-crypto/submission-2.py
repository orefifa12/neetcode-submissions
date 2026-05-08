class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxPrice = prices[0]

        profit = 0

        for i in range(len(prices)):
            if prices[i] <  minPrice:
                minPrice = prices[i]
            else:
                if prices[i] - minPrice > profit:
                    maxPrice = prices[i]
                    profit = maxPrice - minPrice
        
        return profit