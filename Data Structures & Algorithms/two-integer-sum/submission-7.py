class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range (len(nums)):
        #     for j in range (len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]
        
        numDict = {}
        finalArr = []
        for i in range (len(nums)):
            wantedNumber = target - nums[i]
            if wantedNumber not in numDict:
                numDict[nums[i]] = i # put current number for later
            else:
                finalArr = [numDict[wantedNumber], i]

        return finalArr