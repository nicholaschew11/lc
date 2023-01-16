from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        freq = defaultdict(list)
        ans = []
        for i in nums:
            map[i] += 1
        for key, val in map.items():
            freq[val].append(key)

        c = len(nums)
        while (c >= 0):
            if c in freq:
                for i in freq[c]:
                    if k == 0:
                        break
                    ans.append(i)
                    k -= 1
            c -= 1
        return ans
