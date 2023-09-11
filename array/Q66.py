def plusOne(digits: List[int]) -> List[int]:
    """
    Increment the large integer by one and return the resulting array of digits.

    >>> l = [2, 4, 6, 8]
    >>> plusOne(l)
    [2, 4, 6, 9]

    """
    integer_value = 0
    for val in digits:
        integer_value = integer_value * 10 + val
        
    sum_value = integer_value + 1
    final_str = str(sum_value)
    final_lst = [int(i) for i in final_str]
    return final_lst
