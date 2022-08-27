class Solution:
    def reverseBits(self, n: int) -> int:
      """
      https://leetcode.com/problems/reverse-bits/
      
      Reverse bits of a given 32 bits unsigned integer.


      """
        str_n = bin(n)[2:].zfill(32)
        rev_n = str_n[::-1]
        int_number = int(rev_n, 2)
        
        return int_number
