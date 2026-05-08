# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if (p and not q) or (not p and q): return False

        if self.isSameTree(p.left, q.left) == True and self.isSameTree(p.right,q.right) == True and (p.val == q.val): 
            return True
        return False


        