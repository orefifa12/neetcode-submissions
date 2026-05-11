class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        freqDict = {} #dict number : freq
        for number in nums: #assess freq
            if number not in freqDict:
                freqDict[number] = 1
            else:
                freqDict[number] += 1

        frequencies = sorted(freqDict.items(), key = lambda x: x[1], reverse = True) #sort values
        maxNum = frequencies[0][0]

        if frequencies[0][1] < n/2:#check value > n/2 
            return None
        else:
            return maxNum#return key
