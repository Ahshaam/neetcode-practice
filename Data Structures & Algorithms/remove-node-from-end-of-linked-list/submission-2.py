# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        
        cur = head
        prev = dummy
        idx = length - n
        for _ in range(idx):
            prev = cur
            cur = cur.next
        
        if not cur:
            prev.next = None
        else:
            prev.next = cur.next
        return dummy.next
        

        

