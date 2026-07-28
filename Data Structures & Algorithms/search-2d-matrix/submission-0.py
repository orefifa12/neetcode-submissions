"""
UNDERSTAND
I: 2-D int arr(sorted least to greatest), int target
    first integer of every subarr > prev first int n = inner length m = number of rows
O: Return True if in matrix
EC: Can there be an empty row?
MATCH
Because it is sorted and we are looking for a target, we might be able to leverate binary search
PLAN (ABSTRACK TO 1D)
set l to first digit
set r to last digit

while l <= r:
    mid is array between l and r
    if middle number is what we want return
    if number is higher than first number in r, set l = mid
    if number is lower, set r to 1 minus middle
ret -1
EVALUATE
O(m log n) time
O(1) Space
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(matrix_num,target):
            l = 0
            r = len(matrix[matrix_num])-1

            current_level = matrix[matrix_num]
            while l <= r:
                mid = (r+l)//2

                if current_level[mid] == target:
                    return True
                elif current_level[mid] < target:
                    l = mid + 1
                elif current_level[mid] > target:
                    r = mid - 1
            
        m = len(matrix)
        for i in range(len(matrix)):
            if binarySearch(i, target):
                return True
        return False