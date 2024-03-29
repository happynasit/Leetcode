class Solution:
    def isHappy(self, n: int) -> bool:
      """
      https://leetcode.com/problems/happy-number/
      A happy number is a number defined by the following process:

      Starting with any positive integer, replace the number by the sum of the squares of its digits.
      Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
      Those numbers for which this process ends in 1 are happy.
      """
        while n > 4:
            n = sum([int(value)**2 for value in str(n)])
        if n == 1:
            return True
        else:
            return False
