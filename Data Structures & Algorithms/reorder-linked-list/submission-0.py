# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = None
        slow = head
        fast = head
        
        while ( fast and fast.next):
            slow = slow.next
            fast = fast.next.next 
        
        middle = slow

        next_half = middle.next

        middle.next = None
        prev =  None
        curr = next_half

        while(curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        while(prev is not None):
            f = head.next
            p = prev.next
            head.next = prev
            prev.next = f
            head = f
            prev = p
            


            

        

        