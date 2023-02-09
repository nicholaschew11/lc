class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(heights, visited, i, j, height):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
                return

            if visited[i][j] or heights[i][j] < height:
                return

            visited[i][j] = True

            dfs(heights, visited, i + 1, j, heights[i][j])
            dfs(heights, visited, i - 1, j, heights[i][j])
            dfs(heights, visited, i, j + 1, heights[i][j])
            dfs(heights, visited, i, j - 1, heights[i][j])

        ans = []
        pacific = [[False for x in range(len(heights[0]))] for y in range(len(heights))]
        atlantic = [[False for x in range(len(heights[0]))] for y in range(len(heights))]

        for i in range(len(heights)):
            dfs(heights, pacific, i, 0, float('-inf'))
            dfs(heights, atlantic, i, len(heights[0]) - 1, float('-inf'))

        for j in range(len(heights[0])):
            dfs(heights, pacific, 0, j, float('-inf'))
            dfs(heights, atlantic, len(heights) - 1, j, float('-inf'))

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans