def lengthOfLastWord(self, s: str) -> int:
  '''
  completed EASY #Q58 - return the length of the last word in the string
  '''
  s = s.split()
  return len(s[-1])
