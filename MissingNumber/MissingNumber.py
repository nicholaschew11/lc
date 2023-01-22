from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums), 0, -1)) - sum(nums)