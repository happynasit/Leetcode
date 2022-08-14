class Solution:
    def singleNumber(self, nums: list[int]) -> int:
      """
      Given an integer array nums where every element appears three times except for one, which appears exactly once. 
      Find the single element and return it.

      You must implement a solution with a linear runtime complexity and use only constant extra space.


      """
        s = set(nums)
        
        for i in s:
            if nums.count(i) == 1:
                return i
            
        return 0
