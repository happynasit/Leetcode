# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
        """
        curr = head
        prev = head
        if head is not None:
            if head.val == val:
                head = head.next
                curr = head
            else:
                while curr is not None:
                    if curr.val == val:
                        prev.next = curr.next
                        curr = curr.next
                    else:
                        prev = curr
                        curr = curr.next
            return head
