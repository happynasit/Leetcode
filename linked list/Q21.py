# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head = None
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_head = ListNode()

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                list_head.next = list1
                list_head, list1 = list_head.next, list1.next
            else:
                list_head.next = list2
                list_head, list2 = list_head.next, list2.next
        if list1 is not None or list2 is not None:
            if list1 is not None:
                list_head.next = list1
            else:
                list_head.next = list2
        return list_head.next
