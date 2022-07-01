def reverse(self, x: int) -> int:
    """
    COMPLETED medium:  return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit 
    integer range [-231, 231 - 1], then return 0.
    """
    # used the absolute value of x to find its reverse
    abs_value = abs(x)
    rev_value = 0
    while abs_value > 0:
        rev_value = rev_value * 10 + (abs_value % 10)
        abs_value = abs_value // 10
    # if the number is not in between then return 0
    if -2 ** 31 <= rev_value <= (2 ** 31) - 1:
        # if the number was positive or negative, then it returns the reversed number with that sign
        if x >= 0:
            return rev_value
        else:
            return -rev_value
    else:
        return 0