# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
#         curr = head
#         len = 0 
#         while curr:
#             len += 1 
#             curr = curr.next

#         curr =head
        
#         if len == n:
#             if curr.next:
#                 head = curr.next
#                 return head
#             else:
#                 return None
#     # n =2 
#     # N- n = 5 - 2 =3 
#     # 1 2 3 4 5 
#         while curr:
#             len -= 1
#             if len == n:
#                 # need to remove the next one 
#                 curr.next = curr.next.next
#                 break;
    

#             curr = curr.next
#         return head

            
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
        
        removeIndex =  len- n
        if removeIndex == 0:
            return head.next
      
    # n =2 
    # N- n = 5 - 2 =3 
    # 1 2 3 4 5 
        idx = 0
        while curr:
            if idx + 1 == removeIndex:
                curr.next = curr.next.next
                return head;
            idx += 1
            # if len == n:
            #     # need to remove the next one 
            #     curr.next = curr.next.next
            #     break;
    

            curr = curr.next
        return head

            
