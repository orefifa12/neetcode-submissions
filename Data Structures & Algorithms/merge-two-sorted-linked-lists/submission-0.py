# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #start with 2 pointers
        #store temps for both list
        #comparison
        #reassign pointers

        finalList = ListNode()
        tail = finalList

        redPoint = list1
        bluePoint = list2

        while redPoint != None and bluePoint != None:
            # redTemp = redPoint.next
            # blueTemp = blueTemp.next

            if redPoint.val <= bluePoint.val:
                tail.next = redPoint
                redPoint = redPoint.next
            
            elif bluePoint.val < redPoint.val:
                tail.next = bluePoint
                bluePoint = bluePoint.next


            tail = tail.next

        if redPoint != None:
            tail.next = redPoint

        if bluePoint != None:
            tail.next = bluePoint
        
        return finalList.next

            