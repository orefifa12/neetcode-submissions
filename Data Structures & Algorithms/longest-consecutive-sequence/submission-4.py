"""
UNDERSTAND
I: array of type int
O: Longes consecutive seq (1,2,3)
EC: Empty Area

Plan:
Time:O(n log n) Space: O(1)

Sort nums
var count
var currcount
loop through nums
if next number greater than prev by 1
    inc currcount 
else
    check if currcount > count 
    reset currcount

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return len(nums)
        # nums.sort()

        # count = 1
        # curr_streak = 1

        # for i in range(len(nums)-1): #loop through till end
        #     if nums[i+1] == nums[i]:
        #         i += 1
        #         continue
        #     elif nums[i+1] - nums[i] <= 1:
        #         curr_streak += 1
        #     else:
        #         count = max(curr_streak, count)
        #         curr_streak = 1
        #     i += 1

        # return max(curr_streak, count) 

        numSet = set(nums)
        longest = 0

        for number in numSet:
            if (number-1) not in numSet:
                length = 1
                while (number + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest
        
        