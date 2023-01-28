class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.in_order(root, float('-inf'), float('inf'))

    def in_order(self, root, lower, upper):
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return self.in_order(root.left, lower, root.val) and self.in_order(root.right, root.val, upper)