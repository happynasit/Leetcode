def searchInsert(nums: List[int], target: int) -> int:
    """
    COMPLETED: 
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. If not, return the index 
    where it would be if it were inserted in order.

    >>> lst = [2, 4, 6, 8, 10]
    >>> searchInsert(lst, 5)
    2

    >>> searchInsert(lst, 11)
    5
    """
    if target in nums:
        return nums.index(target)
    else:
        if target <= min(nums):
            return 0
        elif target >= max(nums):
            return len(nums)
        else:
            for index in range(len(nums)):
                if nums[index] <= target <= nums[index + 1]:
                    return index + 1