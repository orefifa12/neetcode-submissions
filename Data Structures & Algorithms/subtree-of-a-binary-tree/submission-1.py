# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
UNDERSTAND
I: given two BTs (root & subroot)
O: if subroot is within root
EC: if root and not st return triv true
if root empty return False

MATCH
Traversal to check whats in
PLAN
EC
Check if whole root is subroot
do rec on left and right
EVALUATE
"""
class Solution:   
    def isSameTree(self, root, newTree):
        if root is None and newTree is None:
            return True
        if (root and not newTree) or (not root and newTree):
            return False

        if root.val == newTree.val:
            return (self.isSameTree(root.left, newTree.left) and self.isSameTree(root.right, newTree.right))
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #EC
        if root and not subRoot:
            return True
        if subRoot and not root:
            return False

        
        if root.val == subRoot.val:
            if (self.isSameTree(root.left, subRoot.left)) and (self.isSameTree(root.right, subRoot.right)):
                return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)