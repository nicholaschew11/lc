from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        position = defaultdict(int)
        maxLength = 0
        for i, val in enumerate(s):
            start = max(start, position[val])
            maxLength = max(maxLength, i - start + 1)
            position[val] = i + 1
        return maxLength