class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = float('-inf')
        maxEndHere = 0
        for i in range(len(nums)):
            maxEndHere += nums[i]
            if maxSoFar < maxEndHere:
                maxSoFar = maxEndHere
            if maxEndHere < 0:
                maxEndHere = 0
        return maxSoFar