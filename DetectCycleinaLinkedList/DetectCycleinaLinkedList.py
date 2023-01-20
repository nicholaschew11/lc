from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = set()
        temp = head
        while (temp):
            if (temp in m): return True
            m.add(temp)
            temp = temp.next
        return False