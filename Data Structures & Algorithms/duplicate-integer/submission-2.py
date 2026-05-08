class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {} #O(1)
        for number in nums: #O(n)
            if number in dict: #O(1)
                return True
            dict[number] = True #O(1)
        return False#O(1)
         