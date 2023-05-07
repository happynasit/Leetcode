def majorityElement(nums: list[int]) -> int:
    """
    Completed EASY:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than 
    ⌊n / 2⌋ times. You may assume that the majority element always 
    exists in the array.

    """
    new_lst = []
        
    for i in nums:
        if i not in new_lst:
            new_lst.append(i)
    
    for val in new_lst:
        if nums.count(val) > (len(nums) // 2):
            return val
