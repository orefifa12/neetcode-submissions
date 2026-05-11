class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ### Method 1
        n = len(nums)
        maxNumRet = [nums[0], 0] #num freq

        freqDict = {} #dict number : freq
        for number in nums: #assess freq O(n)
            if number not in freqDict:
                freqDict[number] = 1
            else:
                freqDict[number] += 1
                if freqDict[number] > maxNumRet[1]:
                    maxNumRet = [number, freqDict[number]]

        return maxNumRet[0]  #return key
