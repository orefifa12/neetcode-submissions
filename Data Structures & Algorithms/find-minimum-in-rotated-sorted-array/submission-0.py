"""
UNDERSTAND:
I: rotated arr
O: return the min number
EC: 

MATCH
Bin Search

PLAN
Normal has r > l
while r < l

set up r,l
calc mid
if r < l
change bounds
then normal binsearch 
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
        
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid
        
        return nums[l]
        