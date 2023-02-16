from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return "n"
        ans = [str(root.val)]
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                ans.append(str(node.left.val))
                q.append(node.left)
            else:
                ans.append("n")
            if node.right:
                ans.append(str(node.right.val))
                q.append(node.right)
            else:
                ans.append("n")
        return "/".join(ans)

    def deserialize(self, data):
        data = data.split("/")
        n = 0
        if data[n] == "n":
            return None
        root = TreeNode(int(data[n]))
        n += 1
        q = deque([root])
        while q:
            node = q.popleft()
            if data[n] != "n":
                node.left = TreeNode(int(data[n]))
                q.append(node.left)
            n += 1
            if data[n] != "n":
                node.right = TreeNode(int(data[n]))
                q.append(node.right)
            n += 1
        return root