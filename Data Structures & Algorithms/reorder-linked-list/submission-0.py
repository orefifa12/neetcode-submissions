# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
UNDERSTAND
i: head of linkedlist w/ 0 indexing
o: [0, n-1, 1, n-2]
EC:If there is only 2 nodes return that node 
MATCH
slow fast rev
PLAN
Use slow fast to get to middle of list (as well as track length)
reverse second half of list
move to middle of list
interwieve and move pointers
EVALUATE
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(newhead):
            if newhead is None:
                return None
            
            if newhead.next is None:
                return newhead

            curr = newhead
            prev = None
            while curr:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        ptr = head
        if ptr is None: 
            return None

        slow = fast = ptr
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow.next
        slow.next = None

        slow = reverseList(second_half)

        curr = head
        while curr and slow:
            temp = curr.next
            temp2 = slow.next
            curr.next = slow
            slow.next = temp
            slow = temp2
            curr = temp


                