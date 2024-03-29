# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/description/
        Given the root of a binary tree, return the inorder traversal of its nodes' values.
        """
        l = []
        if root is not None:
            l.extend(self.inorderTraversal(root.left))
            l.append(root.val)
            l.extend(self.inorderTraversal(root.right))
        return l
