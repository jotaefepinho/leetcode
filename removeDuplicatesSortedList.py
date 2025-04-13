class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = head.val
        node = head
        while node.next != None:
            if val == node.next.val:
                node.next = node.next.next
            if node.next != None: 
                node = node.next
                val = node.val
            

        return head

