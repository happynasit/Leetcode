class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        https://leetcode.com/problems/number-of-1-bits/

        Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the 
        Hamming weight).

        """
        count = 0
        # bin() returns a binary version of a value
        for i in str(bin(n)):
            if i == '1':
                count = count + 1
        return count