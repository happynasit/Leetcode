def isPerfectSquare(num: int) -> bool:
    """
    Completed EASY:
    Given a positive integer num, write a function which returns True 
    if num is a perfect square else False.
    Follow up: Do not use any built-in library function such as sqrt.
    """
    if num < 0:
        return False
    else:
        value = num ** 0.5
        if value - int(value) == 0:
            return True
        else:
            return False
        
