class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      """
      https://leetcode.com/problems/squares-of-a-sorted-array/
      
      Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
      """
        lst = [i**2 for i in nums]
        lst.sort()
        return lst
