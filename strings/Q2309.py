class Solution:
    def greatestLetter(self, s: str) -> str:
      """
      https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
      
      Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. 
      The returned letter should be in uppercase. If no such letter exists, return an empty string.


      """
        max_letter = ""
        
        for i in set(s.upper()):
            if i in s and i.lower() in s:
                max_letter = max(max_letter, i)
        return max_letter
