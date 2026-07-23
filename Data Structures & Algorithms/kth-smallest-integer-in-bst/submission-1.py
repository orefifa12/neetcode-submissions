# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#iterative
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while current or stack:

            # go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # visit node
            current = stack.pop()
            count += 1
            if count == k:
                return current.val      # stop as soon as we hit kth

            # move to right subtree
            current = current.right

        return -1   # k out of bounds