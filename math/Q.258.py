def addDigits(num: int) -> int:
    """
    COMPLETED EASY: Q258. Add Digits
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
    
    >>> num = 38
    >>> addDigits(num)
    2
    
    >>> num = 0
    >>> addDigits(num)
    0
    """
    sum_ = 0
        
    while num != 0:
        sum_ = sum_ + (num % 10)
        num = num // 10

    if len(str(sum_)) != 1:
        return addDigits(sum_)
    else:
        return sum_
