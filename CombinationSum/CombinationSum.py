class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for i in range(1, target + 1):
            dp[i] = 0
            for j in nums:
                dp[i] += dp.get(i - j, 0)

        return dp[target]
        