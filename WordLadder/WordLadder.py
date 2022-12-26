from typing import List
from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        depth = {beginWord : 1}
        q = deque()
        q.appendleft(beginWord)
        while q:
            curr = q.popleft()
            for i in range(len(curr)):
                characters = list(curr)
                for c in string.ascii_lowercase:
                    characters[i] = c
                    modified = "".join([str(i) for i in characters])
                    if modified in s and modified not in depth:
                        depth[modified] = depth[curr] + 1
                        if modified == endWord:
                            return depth[modified]
                        q.append(modified)
        return 0