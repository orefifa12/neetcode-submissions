class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n^2)
        # numsLen = len(nums)
        # for i in range(numsLen):
        #     for j in range(numsLen):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        #O(n)

        #key = number #value = index
        hashmap = {}

        numsLen = len(nums)
        for i in range(numsLen):
            canidate = target - nums[i]
            if canidate in hashmap:
                return [hashmap[canidate], i]
            else:
                hashmap[nums[i]] = i
