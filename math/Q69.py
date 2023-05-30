class Solution:
    def mySqrt(self, x: int) -> int:
      """
      Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
      """
        if x==0:
            return 0
        elif x==1:
            return 1
        else:
            for i in range(1,x+1):
                if i*i > x:
                    return i-1
