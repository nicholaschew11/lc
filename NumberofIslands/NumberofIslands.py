class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            # out of bounds
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return

            # water
            if grid[i][j] == '0':
                return

            # mark as water to avoid searching same graph again
            grid[i][j] = '0'

            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
        return ans