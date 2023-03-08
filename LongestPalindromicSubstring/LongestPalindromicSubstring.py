class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.ans = ""
        self.maxLength = 0

        def checker(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > self.maxLength:
                    self.ans = s[left : right + 1]
                    self.maxLength = right - left + 1
                left -= 1
                right += 1

        for c in range(len(s)):
            checker(s, c, c)
            checker(s, c, c + 1)

        return self.ans