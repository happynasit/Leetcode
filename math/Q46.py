class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations.
        """
        l = []
        if len(nums) == 1:
            return [nums.copy()]
        
        # Using recursion
        for i in range(len(nums)):
            n = nums.pop(0)
            sub_ = self.permute(nums)

            for value in sub_:
                value.append(n)

            l.extend(sub_)
            nums.append(n)
        return l
