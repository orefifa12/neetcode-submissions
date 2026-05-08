class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # go through each and check if its in the save dict, if it s return true
        # Turn into a dict check lengths
        numsDict = list(set(nums))
        return not(len(numsDict) == len(nums))