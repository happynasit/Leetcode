def myPow(x: float, n: int) -> float:
    """
    Completed MEDIUM: 
    Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

    """
    if n >= 0:
        return x ** n
    elif n < 0:
        return x ** n