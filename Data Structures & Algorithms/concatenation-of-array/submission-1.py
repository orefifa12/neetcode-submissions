class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # totalLen = 2 * len(nums)
        # ans = [None] * totalLen
        # for j in range(len(nums)):
        #     for i in range(len(nums)):
        #         ans[i] = nums[i]
        #     ans[j+i+1] = nums[j]
        ans = nums + nums
        return ans