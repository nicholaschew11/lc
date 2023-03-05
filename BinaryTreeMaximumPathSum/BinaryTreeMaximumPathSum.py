from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def helper(node):
            if not node:
                return 0

            leftAmt = max(helper(node.left), 0)
            rightAmt = max(helper(node.right), 0)
            self.ans = max(self.ans, node.val + leftAmt + rightAmt)

            return node.val + max(leftAmt, rightAmt)

        helper(root)
        return self.ans