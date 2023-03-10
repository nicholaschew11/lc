from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.completes_word = False

    def insertWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.completes_word = True

    def prune(self, word) -> None:
        node = self
        deleteList = []
        
        for c in word:
            deleteList.append((node, c))
            node = node.children[c]

        for parent, child in reversed(deleteList):
            target = parent.children[child]
            if len(target.children) == 0:
                del parent.children[child]
            else:
                return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        root = TrieNode()
        visited = set()
        for w in words:
            root.insertWord(w)

        def dfs(i, j, node, word):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if (i, j) in visited or board[i][j] not in node.children:
                return

            visited.add((i, j))

            node = node.children[board[i][j]]
            word += board[i][j]
            if node.completes_word:
                ans.append(word)
                node.completes_word = False
                root.prune(word)

            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)

            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, "")
        
        return ans