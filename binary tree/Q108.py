# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
      """
      Given an integer array nums where the elements are sorted in ascending order, convert it to a 
      height-balanced binary search tree.
      """
        if nums == []:
            return None
        else:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])

            # we have the middle element that can be set as the root of the tree

            # Recursion
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])

            return root
