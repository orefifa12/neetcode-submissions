"""
UNDERSTAND
i: array nums where i is the number of money i house has
o: Max money rob without alerting police(cant do adjacent house)
EC: dp[1] dp[2] = 0 bc you cant rob them back to back
MATCH
Dynamic programing because you want to keep track of the max from the previous houses to find max
PLAN
BC: dp[1] = nums[i] dp[2] = nums[i]
State : dp[i] signifies the max money possible including this house and no other houses which are back to back
Recurrence Case: if robbable aka not adjacent dp[i] = dp[i-2] + nums[i] else dp[i] = dp[i-1]
Final Solution dp[i-1]
EVAL
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * (len(nums) + 1)
        
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, len(nums)+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        return dp[len(nums)]