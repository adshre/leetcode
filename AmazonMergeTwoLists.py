class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            else :
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        while l1 is None and l2 is not None :
            l3.next = l2
            l2 = l2.next
            l3 = l3.next
        while l1 is not None and l2 is None :
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        return head.next
        
        
            OR
            
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else :
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 if l1 is not None else l2
        return head.next
