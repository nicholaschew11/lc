class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetMap = defaultdict(int)
        freqMap = defaultdict(int)
        for c in t:
            targetMap[c] += 1
        
        ans = ""
        minLength = float('inf')
        count = len(t)
        left = 0

        for right in range(len(s)):
            if s[right] in targetMap:
                freqMap[s[right]] += 1
                if freqMap[s[right]] <= targetMap[s[right]]:
                    count -= 1
            while count == 0:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    ans = s[left : right + 1]
                if s[left] in targetMap:
                    freqMap[s[left]] -= 1
                    if freqMap[s[left]] < targetMap[s[left]]:
                        count += 1
                left += 1
        return ans