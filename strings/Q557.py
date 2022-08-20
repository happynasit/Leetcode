def reverseWords(self, s: str) -> str:
  '''
  Completed Q557- reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
  '''
  s2 = ''
  # splitting the words into a list
  l = s.split()
  for string in l:
      # reversing the characters in each word and adding into a new string s2
      s2 = s2 + string[::-1]
      s2 = s2 + ' '
  return s2[:-1]
