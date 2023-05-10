# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, return the preorder traversal of its nodes' values.
        """
        l = []
        if root is not None:
	    l.append(root.val)
            l.extend(self.inorderTraversal(root.left))
            l.extend(self.inorderTraversal(root.right))
        return l
