"""
UNDERSTAND
I: int arr with i meaning the day
O: return higest profit
EC: Can only sell after bought date
    if only one price return 0
MATCH
Sliding window to find which day bought and sell winow is max
PLAN
EC: if only one price ret 0

set buy to day 1 and sell to day 2
calc curr profit
loop through prices
if curent day has a lower price than buy update buy
else if sell is higher than prev sell update max profit
ret max prof
EVALUATE
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        buy_day = 0
        sell_day = 1

        max_profit = max(prices[sell_day] - prices[buy_day], 0)

        for i in range(1, len(prices)):
            current_profit = 0
            if prices[i] < prices[buy_day]:
                buy_day = i
                if buy_day < len(prices)-1:
                    sell_day = buy_day + 1
                    current_profit = prices[sell_day] - prices[buy_day]   
            else:
                if prices[i] > prices[sell_day]:
                    sell_day = i
                    current_profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, current_profit)
        
        return max_profit
        