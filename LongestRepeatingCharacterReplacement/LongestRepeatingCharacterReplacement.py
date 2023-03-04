class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        letters = [0] * 26
        start = 0
        max_letter = 0

        for end in range(len(s)):
            letters[ord(s[end]) - ord('A')] += 1
            max_letter = max(max_letter, letters[ord(s[end]) - ord('A')])
            window_length = end - start + 1

            if max_letter + k < window_length:
                letters[ord(s[start]) - ord('A')] -= 1
                start += 1

            ans = max(ans, end - start + 1)

        return ans