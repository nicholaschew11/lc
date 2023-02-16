class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        dict = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif not stack or stack.pop() != dict[c]:
                return False
        return not stack
        