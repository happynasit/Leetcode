class Solution:
    def sumOfMultiples(self, n: int) -> int:
      """
      https://leetcode.com/problems/sum-multiples/description/
      """
        sum_ = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum_ = sum_ + i
        return sum_
