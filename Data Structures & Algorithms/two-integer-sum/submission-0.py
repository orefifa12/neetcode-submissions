class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #learn list comp
        numbers = {}
        
        for index, num in enumerate(nums):
            potentialTarget = target - num

            if potentialTarget in numbers:
                return [numbers.get(potentialTarget), index]
            numbers[num] = index