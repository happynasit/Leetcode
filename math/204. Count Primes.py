def countPrimes(n: int) -> int:
  """
  COMPLETED MEDIUM:
  Given an integer n, return the number of prime numbers that are strictly less than n.
  
  >>> aa = 0
  >>> countPrimes(aa)
  0
  
  >>> a = 2
  >>> countPrimes(a)
  0
  
  """
    nums_till_n = 0
        
    i = 0
    while i < n:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0 :
                count = count + 1
        if count == 2:
            nums_till_n = nums_till_n + 1
        i = i + 1
                    
    return nums_till_n
