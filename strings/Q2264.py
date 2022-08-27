class Solution:
    def largestGoodInteger(self, num: str) -> str:
      """
      https://leetcode.com/problems/largest-3-same-digit-number-in-string/
      
      Return the maximum good integer as a string or an empty string "" if no such integer exists.
      """
        max_ = ''
        for index in range(1, len(num) - 1):
            if num[index] == num[index-1] and num[index] == num[index+1]:
                if max_ == '':
                    max_ = num[index-1: index+2]
                else:
                    max_ = max(int(max_), int(num[index-1: index+2]))
                    
        return str(max_)
