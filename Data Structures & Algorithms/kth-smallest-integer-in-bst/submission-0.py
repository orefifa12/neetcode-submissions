# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def isChild(root):
            return root and root.left == None and root.right == None
        
        def inOrder(roots):
            if roots is None:
                return []
            
            return inOrder(roots.left) + [roots.val] + inOrder(roots.right)

        ordered_list = inOrder(root)

        return ordered_list[k-1]
            

        
        