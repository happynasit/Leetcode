class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Completed EASY:
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.


        """
        for index in range(len(nums)):
            
            new = nums[:]
            new[index] = '_'
            
            val_i = target - nums[index]
            if val_i in new:
                final_pair = [new.index(val_i), index]
        return final_pair
