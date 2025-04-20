# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        revHead = reverseList(head.next)
    
        head.next.next = head
        
        head.next = None
        
        return revHead

##Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            temp = curr.next

            curr.next = prev

            prev = curr
            curr = temp
        
        return prev