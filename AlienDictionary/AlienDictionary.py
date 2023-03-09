from collections import defaultdict, deque
from typing import List

class Solution:
    def alien_order(self, words: List[str]) -> str:
        ans = ""
        graph = defaultdict(set)
        in_degree = {}
        for w in words:
            for c in w:
                in_degree[c] = 0

        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].add(second[j])
                        in_degree[second[j]] += 1
                    # only need to compare the characters upto the point where they differ
                    break

        # add all nodes with no incoming edges
        q = deque([c for c in in_degree if in_degree[c] == 0])
        # bfs topological sort
        while q:
            c = q.popleft()
            ans += c
            for n in graph[c]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)

        if len(ans) < len(in_degree): # cycle in graph
            return ""

        return ans

