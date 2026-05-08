# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        restOfList = self.reverseList(head.next)

        temp = restOfList
        while temp.next != None:
            temp = temp.next
        
        head.next = None
        temp.next = head

        return restOfList
        
        
        