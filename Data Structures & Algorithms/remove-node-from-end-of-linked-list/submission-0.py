# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        len = 0 
        while curr:
            len += 1 
            curr = curr.next

        curr =head
        if len == n:
            if curr.next:
                head = curr.next
                return head
            else:
                return None
    
    
        while curr:
            len -= 1
            if len == n:
                # need to remove the next one 
                curr.next = curr.next.next
                break;
    

            curr = curr.next
        return head

            
