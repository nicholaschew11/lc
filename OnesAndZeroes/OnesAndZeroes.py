from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n + 1) for i in range(m + 1)]
        for s in strs:
            zeroCount = s.count('0')
            oneCount = s.count('1')
            for i in reversed(range(zeroCount, m + 1)):
                for j in reversed(range(oneCount, n + 1)):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroCount][j - oneCount])
        return dp[m][n]