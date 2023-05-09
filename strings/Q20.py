class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        
        An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.
        """
        opening_parenthesis = []
        opening_brackets = ('(', '[', '{')
        for letter in s:
            if letter in opening_brackets:
                # Appends only the opening brackets and checks if it is valid or not.
                opening_parenthesis.append(letter)
            else:
                if not opening_parenthesis:
                    return False
                # If the closing parenthesis and the corresponding opening parenthesis is in the list, then it pops
                if letter == ')' and opening_parenthesis[-1] == '(':
                    opening_parenthesis.pop()
                elif letter == ']' and opening_parenthesis[-1] == '[':
                    opening_parenthesis.pop()
                elif letter == '}' and opening_parenthesis[-1] == '{':
                    opening_parenthesis.pop()
                else:
                    return False
        # At the end, the opening_parenthesis should have an empty list.
        # It indicates that it is a valid parentheses.
        return opening_parenthesis == []
