# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      """
      You are given the heads of two sorted linked lists list1 and list2.
      Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
      Return the head of the merged linked list.
      """
        list_head = ListNode()

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                self.insert(list1.val, list_head)
                list_head = list_head.next
                list1 = list1.next
            else:
                self.insert(list2.val, list_head)
                list_head = list_head.next
                list2 = list2.next
        if list1 is not None or list2 is not None:
            if list1 is not None:
                list_head.next = list1
            else:
                list_head.next = list2
        return list_head
        
    def insert(self, num: int, head: Optional[ListNode]):
        """
        Inserts a node at the end of the linked list
        """
        node = ListNode(num)
        if head is None:
            head.val = num
            head.next = None
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next

            curr.next = node
