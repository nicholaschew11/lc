class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        stack = [node]
        clone = {node.val: Node(node.val, [])}
        
        while stack:
            curr = stack.pop()
            currClone = clone[curr.val]
            for n in curr.neighbors:
                if n.val not in clone:
                    clone[n.val] = Node(n.val, [])
                    stack.append(n)
                currClone.neighbors.append(clone[n.val])

        return clone[node.val]