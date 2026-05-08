# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: return False
        fpointer = spointer = head

        while fpointer != None and fpointer.next!= None:
            spointer = spointer.next
            fpointer = fpointer.next.next
            
            if fpointer == spointer:
                return True
                
        
        return False
