from typing import List, Optional
from collections import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#priority queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        head = ListNode(0)
        curr = head
        pq = []
        
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(pq, (lst.val, i))
        
        while pq:
            val, i = heapq.heappop(pq)
            curr.next = ListNode(val)
            curr = curr.next
            
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
            
        return head.next
    
#sorting
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        allNodes = []
        head = temp = ListNode(0)
        
        for lst in lists:
            while lst:
                allNodes.append(lst.val)
                lst = lst.next
        
        for n in sorted(allNodes):
            temp.next = ListNode(n)
            temp = temp.next

        return head.next