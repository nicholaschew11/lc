class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            a = ''.join(sorted(s))
            if a not in dictionary:
                dictionary[a] = [s]
            else:
                dictionary[a].append(s)
        return dictionary.values()