import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = []
        heapq.heapify(lst)
        for n in nums:
            if len(lst) < k:
                heapq.heappush(lst, n)
            elif n > lst[0]:
                heapq.heapreplace(lst, n)
        return lst[0]