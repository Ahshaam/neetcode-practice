# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow.next = None
        
        prev = None
        cur = tail
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        front_ptr = head
        tail_ptr = prev
        while front_ptr and tail_ptr:
            tmp1 = front_ptr.next
            tmp2 = tail_ptr.next
            front_ptr.next = tail_ptr
            tail_ptr.next = tmp1
            front_ptr = tmp1
            tail_ptr = tmp2
        
            

