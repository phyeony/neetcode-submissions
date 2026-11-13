# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        merged_head = None
        l1_head = list1
        l2_head = list2
        # set the very first head
        if l1_head != None and l2_head != None:
            if l1_head.val > l2_head.val:
                merged_head = l2_head
                l2_head = l2_head.next
            else:
                merged_head = l1_head
                l1_head = l1_head.next
        elif l1_head != None:
            merged_head = l1_head
            l1_head = l1_head.next
        elif l2_head != None:
            merged_head = l2_head
            l2_head = l2_head.next
        else:
            return merged_head

        curr = merged_head
        while l1_head != None and l2_head != None:
            if l1_head.val < l2_head.val:
                curr.next = l1_head
                curr = curr.next
                l1_head = l1_head.next
            else:
                curr.next = l2_head
                curr = curr.next
                l2_head = l2_head.next
        if l1_head != None:
            curr.next = l1_head
        elif l2_head != None:
            curr.next = l2_head

        return merged_head
