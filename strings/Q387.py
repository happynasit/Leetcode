class Solution:
    def firstUniqChar(self, s: str) -> int:
      """
      https://leetcode.com/problems/first-unique-character-in-a-string/
      
      Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
      
      
      """
        # counter function creates a dictionary where the keys is the characters of the string and the values are its number of occurences
        d = Counter(s)
        
        for key in d:
            if d[key] == 1:
                return s.index(key)
        return -1
   
