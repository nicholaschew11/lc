class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
            else:
                newMax = max(n * currMax, n * currMin, n)
                newMin = min(n * currMax, n * currMin, n)
                currMax, currMin = newMax, newMin
                ans = max(ans, currMax)
        return ans