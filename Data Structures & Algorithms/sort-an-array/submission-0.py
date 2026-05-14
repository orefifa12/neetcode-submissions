class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ### Method 1 ### Mergesort
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        leftSorted = self.sortArray(left)
        rightSorted = self.sortArray(right)
        
        #------------- Merge-------------------
        i = 0 # left pointer
        j = 0 # right pointer

        # set a final arr
        finalArr = []

        while (i < len(leftSorted) and j < len(rightSorted)):
            if leftSorted[i] < rightSorted[j]:
                finalArr.append(leftSorted[i]) # put the lower number into final
                i += 1
            else:  # put the lower number into final
                finalArr.append(rightSorted[j])
                j += 1
        
        while (i < len(leftSorted)):
            finalArr.append(leftSorted[i])
            i += 1
        while (j < len(rightSorted)):
            finalArr.append(rightSorted[j])
            j += 1

        return finalArr