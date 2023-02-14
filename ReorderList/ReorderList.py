class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        first = head
        second = prev

        while first and second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext

        return head