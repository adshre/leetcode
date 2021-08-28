# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         #baseCondition 
#         if head is None or head.next is None:
#                 return head
#         else:
            
#             newHead = self.reverseList(head.next)
#             tailNode = head.next
#             tailNode.next = head
#             head.next = None
#             return newHead


            #baseCondition :
        if head is None or head.next is None:
            return head
        
        alreadyReversed, curr = head, head.next
        alreadyReversed.next = None
        
        while curr is not None :
            storeptr = curr.next
            curr.next = alreadyReversed
            
            alreadyReversed = curr
            curr = storeptr
            
        return alreadyReversed
            
        
        
        
"""
https://www.youtube.com/watch?v=j6dEFsH_Aqg

"""

        
       
        
        
