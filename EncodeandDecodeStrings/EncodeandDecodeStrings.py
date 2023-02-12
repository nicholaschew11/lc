class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        ans = ""
        for s in strs:
            ans += str(len(s)) + "/" + s
        return ans

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        ans = []
        i = 0
        while i < len(str):
            j = str.index('/', i)
            l = int(str[i:j])
            ans.append(str[j + 1:j + 1 + l])
            i = j + l + 1
        return ans