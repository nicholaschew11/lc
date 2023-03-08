class Solution:
    def countSubstrings(self, s: str) -> int:        
        self.ans = 0

        def checker(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.ans += 1
                left -= 1
                right += 1

        for c in range(len(s)):
            checker(s, c, c)
            checker(s, c, c + 1)

        return self.ans