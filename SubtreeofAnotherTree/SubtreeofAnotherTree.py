# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.checkSubtree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkSubtree(self, childRoot, subRoot):
        if not childRoot and not subRoot:
            return True
        if not childRoot or not subRoot:
            return False
        return childRoot.val == subRoot.val and self.checkSubtree(childRoot.left, subRoot.left) and self.checkSubtree(childRoot.right, subRoot.right)