class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        preProd = [1] * n
        postProd = [1] * n

        # Build prefix product array
        current = 1
        for i in range(n):
            preProd[i] = current
            current *= nums[i]

        # Build postfix product array
        current = 1
        for i in range(n-1, -1, -1):
            postProd[i] = current
            current *= nums[i]

        # Multiply prefix and postfix for final result
        for i in range(n):
            output[i] = preProd[i] * postProd[i]

        return output
