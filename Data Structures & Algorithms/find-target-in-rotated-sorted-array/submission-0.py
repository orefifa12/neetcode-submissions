class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            while l <= r:
                mid = (l+r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        
            return -1
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]: # nonnormal halfk
                l = mid + 1 #good
                
            elif nums[mid] <= nums[r]: #second half
                r = mid 
        #l holds lowest value

        if target >= nums[l] and target <= nums[len(nums)-1]: #lower half
            return binarySearch(l, len(nums)-1)
        else:
            return binarySearch(0, l-1)