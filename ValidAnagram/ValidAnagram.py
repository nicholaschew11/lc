from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        print(m)
        for c in t:
            if c not in m: 
                return False
            m[c] -= 1
            if m[c] == 0:
                m.pop(c)
        return not m