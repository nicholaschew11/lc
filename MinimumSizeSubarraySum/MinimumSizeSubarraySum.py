import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = sys.maxsize
        lp = 0
        ps = 0
        for i in range(len(nums)):
            ps += nums[i]
            while ps >= target:
                m = min(m, i - lp + 1)
                ps -= nums[lp]
                lp += 1

        return 0 if m == sys.maxsize else m