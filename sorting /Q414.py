class Solution:
    def thirdMax(self, nums: List[int]) -> int:
      """
      https://leetcode.com/problems/third-maximum-number/
      
      Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, 
      return the maximum number.
      """
        st = set(nums)
        
        if len(st) < 3:
            return max(st)
        else:
            lst = list(st)
            lst.sort()
            return lst[-3]
        return 0
