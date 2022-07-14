def containsDuplicate(nums: List[int]) -> bool:
    """
    COMPLETED EASY : 
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
    >>> nums = [1,2,3,1]
    >>> containsDuplicate(nums)
    True
    
    >>> nums = [1,2,3,4]
    >>> containsDuplicate(nums)
    False
    
    >>> nums = [1,1,1,3,3,4,3,2,4,2]
    >>> containsDuplicate(nums)
    True
    
    >>> nums = [1]
    >>> containsDuplicate(nums)
    False
    """
    # creating a set of nums and then comparing both the list and set would show whether or not it contains duplicates
    set_nums = set()
    for i in nums:
        set_nums.add(i)
        
    if len(nums) == len(set_nums):
        return False
    else:
        return True
