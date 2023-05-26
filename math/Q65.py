class Solution:
    def isNumber(self, s: str) -> bool:
        """
        checks whether it is a valid number or not
        """
        for i in s:
            if (i.isalpha() and i not in ('e', 'E')) or ( i in "!@#$%^&*()-+?_=,<>/"):
                return False
        
        if len(s) == 2:
            if s[0] == '.':
                if s[1].isdigit():
                    return True
                else:
                    return False
            elif not(s[0].isalpha()):
                if s[1].isalpha():
                    return False
                else:
                    return True
        elif s[len(s) - 1] == 'e' or s[len(s) - 1] == 'E':
            return False
        elif s.isalpha() or (s.isalnum() and (s[0] =='e' or s[0] == 'E')):
            return False
        elif self.isinteger(s) or self.isdecimal(s):
            double_signs = ('--', '+-', '++', '-+', '..')
            l = any([i in s for i in double_signs])
            if l is True:
                return False
            return True 
        else:
            if "e" in s:
                e_index = s.index("e")
                if e_index == 0:
                    return False
                else:
                    return self.isinteger(s[e_index + 1:])
            elif "E" in s:
                e_index = s.index("E")
                if e_index == 0:
                    return False
                else:
                    return self.isinteger(s[e_index + 1:])
        
    
    
    def isinteger(self, s: str) -> bool:
        """
        checks whether a given thing is a integer or not
        """
        for character in s:
            if not(character in ('+', '-') or character.isdigit()):
                return False
        return True
        
        
    def isdecimal(self, s: str) -> bool:
        """
        checks whether a given parameter is a decimal or not
        """
        lst_s = s.split('.')
        for character in s:
            if character in ('+', '-') or lst_s[-1] != '':
                return True
            else:
                return False
