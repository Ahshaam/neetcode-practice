# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        head = ListNode(0)
        ptr = head

        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                ptr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                ptr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            ptr = ptr.next
        
        if ptr1 == None and ptr2 != None:
            ptr.next = ptr2
        elif ptr1 != None and ptr2 == None:
            ptr.next = ptr1
        
        return head.next

        
