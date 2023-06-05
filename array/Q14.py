def longestCommonPrefix(strs: List[str]) -> str:
      """
      Write a function to find the longest common prefix string amongst an array of strings.
      If there is no common prefix, return an empty string ""
      """
      prefix = ""

      # the word with the smallest length will be separately taken
      # the smallest_word's letters will be compared with other words in strs
      smallest_word = min(strs, key = len)

      for index in range(len(smallest_word)):
          if not all(smallest_word[index] == word[index] for word in strs):
              break
          prefix = prefix + smallest_word[index]
      return prefix
