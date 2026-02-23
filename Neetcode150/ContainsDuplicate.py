"""
EASY
Checks if the given array has at least one repeating element.
simply check the length of the list vs the set.
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # there is no fastest way of doing this
        # WORST CASE IF THERE IS AN ARRAY WITH NO REPEATING ELEMENTS, WE HAVE TO
      # ITERATE N TIMES THROUGHOUT THE LIST TO SEE IF THE LIST HAS ANY REPEATING ELEMENT.
      # THATS WHY THE BEST RUNTIME IS LINEAR
        return len(nums) != len(set(nums))
