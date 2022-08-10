class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        """
        https://leetcode.com/problems/unique-morse-code-words/

        Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
        Return the number of different transformations among all words we have.

        """
        alpha = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
                'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 
                'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 
                 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
                'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--",
                'z': "--.."}
        
        set_morse = set()
        for word in words:
            morse = ''
            
            for letter in word:
                morse = morse + alpha[letter]
            set_morse.add(morse)
            
        return len(set_morse)
