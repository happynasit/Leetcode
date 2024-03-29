# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      """
      Given the root of a binary tree, return its maximum depth.
      A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
      """
        if root is None:
            return 0
        else:
            depth_left = self.maxDepth(root.left)
            depth_right = self.maxDepth(root.right)

            if depth_left > depth_right:
                return depth_left + 1
            else:
                return depth_right + 1
