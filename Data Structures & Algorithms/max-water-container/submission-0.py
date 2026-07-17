"""
UNDERSTAND
I: list type int 
O: return max contatiner amount 
EC: len of height < 3 ret 0 bec not 3 dimensions

MATCH
Three Sum, Two Sum

PLAN
x = length (width between 2 bars l and r) two pointer
y = height of lowest bar

Two pointer to find height 
maxDepth
loop through bars
height = width between l and r * min(lowest bar)
maxdepth is bigger between curr height and maxdepth

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 3:
            return min(heights[0],heights[1])

        #two pointer to find height
        l = 0
        max_Depth = 0

        for l in range(len(heights)):
            r = len(heights) - 1
            while l < r:
                current_Depth = (r-l) * min(heights[l], heights[r])
                max_Depth = max(max_Depth, current_Depth)
                r = r - 1
            print(l)
            print(max_Depth)
        
        return max_Depth
        