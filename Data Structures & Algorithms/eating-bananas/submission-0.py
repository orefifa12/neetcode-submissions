"""
UNDERSTAND
N piles of banana, ith pile has piles[i] banana:
    so [3,2] means first pile has 2 bananas
k is banans eating speed
Wants to finish eating all bananas
I: int arr -> piles, h = hours guards come back
O: return min k such that she can eat everything before guards comeback
3 -> 1 hour
6 -> 2 hours
7 -> 2 hours
11 -> 3 hours

MATCH
BinSearch since we want to find some minimum
PLAN
EVALUATE
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkGuess(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile+k-1)//k
            return total_hours

        l, r = 1, max(piles)
        lowest_possible = -1
        while l <= r:
            mid = (r+l) // 2
            perspective_hours = checkGuess(mid)

            if perspective_hours <= h:
                lowest_possible = mid
                r = mid - 1
            elif perspective_hours > h:
                l = mid + 1
        return lowest_possible