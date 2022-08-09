class Solution:
    def findComplement(self, num: int) -> int:
      """
      https://leetcode.com/problems/number-complement/
      
      The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

      For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
      Given an integer num, return its complement.
      """
        # format function returns the binary value without 0b 
        bin_num = format(num, 'b')
        d = {'1': '0', '0': '1'}
        
        s = ''
        s = s.join(d[i] for i in bin_num)
        
    
        return int(s, 2)
