import random
from typing import List
from bisect import bisect_left

class Solution:

    def __init__(self, w: List[int]):
        self.list = [0] * len(w)
        s = 0
        for i, n in enumerate(w):
            s += n
            self.list[i] = s
        print(self.list)
            
    def pickIndex(self) -> int:
        return bisect_left(self.list, random.randint(1, self.list[-1]))