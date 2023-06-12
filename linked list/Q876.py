# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """
      Given the head of a singly linked list, return the middle node of the linked list.

      If there are two middle nodes, return the second middle node.
      """
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            curr = curr.next
        

        if curr 
