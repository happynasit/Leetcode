class Solution:
    def singleNumber(self, nums: list[int]) -> int:
      """
      """
        s = set(nums)
        
        for i in s:
            if nums.count(i) == 1:
                return i
            
        return 0
