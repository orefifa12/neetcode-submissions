class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1. Handle empty list or single node with no cycle
        if not head or not head.next:
            return False
            
        slow = head
        fast = head

        # 2. 'fast' moves twice as fast, so it will hit None first.
        # We check 'fast' (for the current step) and 'fast.next' (for the next step).
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next # Now this is safe because of the while condition
            
            if slow == fast:
                return True
                
        return False