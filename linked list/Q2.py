# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """
        # Converting the linked list into a number in reverse order.
        # l1
        s1 = ""
        curr = l1
        while curr is not None:
            s = s + str(curr.val)
            curr = curr.next
        
        # l2
        s2 = ""
        curr2 = l2
        while curr2 is not None:
            s2 = s2 + str(curr2.val)
            curr2 = curr2.next
        
        # Reversing both the digits that are currently in the string form
        number_1 = int(s1[::-1])
        number_2 = int(s2[::-1])

        # Adding the numbers up
        total_sum = number_1 + number_2
        reversed_sum = (str(total_sum))[::-1]

        if len(reversed_sum) == 1:
            


    
    def insert_node(self, l:Optional[ListNode], a:int):
        """
        Inserts a node at the end of the linked list
        """
        new_node = ListNode(a)
        
        curr = l
        new_node.next = None
        if curr is None:
            return new_node
        
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node
        return l
        
    

    
