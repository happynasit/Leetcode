class Solution:
    def toGoatLatin(self, sentence: str) -> str:
      """
      https://leetcode.com/problems/goat-latin/
      
      You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

      We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

      If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
      For example, the word "apple" becomes "applema".
      
      If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
      For example, the word "goat" becomes "oatgma".
      
      Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
      For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
      
      Return the final sentence representing the conversion from sentence to Goat Latin.


      """
        l = sentence.split()

        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        for index in range(len(l)):
            if l[index][0] in vowels:
                l[index] = l[index] + ('ma' + ('a' * (index + 1)))

            elif l[index][0] not in vowels:
                l[index].replace(l[index][0], '')
                l[index] = l[index][1:] + (l[index][0] + 'ma' + ('a' * (index + 1)))

        ss = ''
        for word in l:
            ss = ss + word
            ss = ss + " "
        return ss.rstrip()
        
