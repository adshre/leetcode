class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        carry = 0
        while l1 or l2 or carry :
            if l1 :
                carry += l1.val
                l1 = l1.next
            if l2 :
                carry += l2.val
                l2 = l2.next
            l3.next = ListNode(carry%10)
            l3 = l3.next
            carry = carry//10
        return head.next
            
            
    
 
Reason :
sum = x +  y + carry
and sum%10 = value
sum// 10 = carry
