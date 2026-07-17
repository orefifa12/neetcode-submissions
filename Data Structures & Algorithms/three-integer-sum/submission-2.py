"""
UNDERSTAND
I: Array of type int
O: triplets where nums[i] + nums[j] + nums[k] == 0

EC: if 3 return if sum == 0
    i,j,k have to be unique

Match 
Two pointers problem

Plan
Address the Edge Case

sort first 
pick pivot as i
do two sum of rest of digits
add to final set
increment i for all numbers

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        #x + y + z = 0 -> y + z = -x -> x = -(y + z)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #two pointer
            l = i + 1
            r = len(nums) - 1

            find = -nums[i]
            while l < r:
                workingSum = (nums[l]+nums[r]) #1
                if workingSum == find: # if triple sum is zero
                    good_tuple = (nums[i],nums[l],nums[r])
                    triplets.add(good_tuple)
                    l += 1
                    r -= 1
                elif workingSum <= find:
                    l += 1
                else:
                    r -= 1



        return list(triplets)
        
        