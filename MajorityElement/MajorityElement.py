from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        ans = None
        for n in nums:
            if c == 0: ans = n
            c += 1 if n == ans else -1
        return ans