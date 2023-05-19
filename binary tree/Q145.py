# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, return the postorder traversal of its nodes' values.
        """
        l = []

        if root is not None:
            l.extend(self.postorderTraversal(root.left))
            l.extend(self.postorderTraversal(root.right))
            l.append(root.val)
<<<<<<< HEAD
        
        return l
=======

        return l




>>>>>>> 2dffd4e7b818945c5ceab44c613d006c1a8079f9
