# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # In order to be the same tree they must have the same traversal
        # So it can be on the basis of the in order traversal.
	"""
	Given the roots of two binary trees p and q, write a function to check if they are the same or not.
	Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
	"""
        p_l = self.inorderTraversal(p)
        q_l = self.inorderTraversal(q)
        return p_l == q_l


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given the root of a binary tree, return the inorder traversal of its nodes' values.
        """
        l = []
        if root is not None:
            l.extend(self.inorderTraversal(root.left))
            l.append(root.val)
            l.extend(self.inorderTraversal(root.right))
        return l
