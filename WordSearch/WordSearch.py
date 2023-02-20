class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx):
            if idx == len(word):
                return True
                
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if visited[i][j] or board[i][j] != word[idx]:
                return False

            visited[i][j] = True

            found = dfs(i + 1, j, idx + 1) or \
                    dfs(i - 1, j, idx + 1) or \
                    dfs(i, j + 1, idx + 1) or \
                    dfs(i, j - 1, idx + 1)

            visited[i][j] = False

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
                if dfs(i, j, 0):
                    return True
        
        return False