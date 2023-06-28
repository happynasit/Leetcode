# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.treeSymmetric(root.left, root.right)
    
    def treeSymmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        """
        checks if the left and the right subtrees of a particular node is symmetric or not
        """

        if left is None and right is None:
            return True
        elif (left is None and right is not None) or (right is None and left is not None):
            return False
        elif left.val != right.val:
            return False
        
        return self.treeSymmetric(left.left, right.right)
