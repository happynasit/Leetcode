class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
      """
      https://leetcode.com/problems/perfect-number/
      
      A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number 
      itself. A divisor of an integer x is an integer that can divide x evenly.

      Given an integer n, return true if n is a perfect number, otherwise return false.
      """
        if num <= 1:
            return False
        else:
            sum_ = 1

            for value in range(2, int(num ** 0.5) + 1):
                if num % value == 0:
                    sum_ = sum_ + ((num//value) + value)
            return sum_ == num