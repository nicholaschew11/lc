class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        def dfs(v):
            visited[v] = True
            for neighbor in adj_list[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        count = 0
        for v in range(n):
            if not visited[v]:
                dfs(v)
                count += 1
    
        return count