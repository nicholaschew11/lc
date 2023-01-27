from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def helper(root):
            if not root:
                return
            helper(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                return
            helper(root.right)

        self.ans = None
        self.k = k
        helper(root)
        return self.ans
