def isPowerOfFour(n: int) -> bool:
  """
  Completed EASY: 
  Given an integer n, return true if it is a power of four. Otherwise, return false.
  An integer n is a power of four, if there exists an integer x such that n == 4^x.

  >>> n = 16
  >>> isPowerOfFour(n)
  True
  
  """
  if n == 1:
      return True
  elif n < 1:
      return False
  elif n % 4 == 0:
      return isPowerOfFour(n // 4)