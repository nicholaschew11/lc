from typing import List
from collections import defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(root):
            visited.add(root)
            for n in graph[root]:
                if n in visited:
                    continue
                dfs(n)

        graph = defaultdict(list)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited = set()
        dfs(0) 
        # must visit all nodes to be connected
        # cycle if n or more edges
        return len(visited) == n and len(edges) == n - 1