class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while (left < right):
            val = min(height[left], height[right])
            ans = max(ans, val * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
