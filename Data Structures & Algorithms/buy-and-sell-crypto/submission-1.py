class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        maxprofit = 0
        

        for i in range(len(prices)):
            price = prices[i]
            if price < buy : # for first update
                buy = price
            
            currentprofit = price - buy
            if currentprofit > maxprofit:
                    maxprofit = currentprofit

        return maxprofit
           
