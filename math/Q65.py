class Solution:
    def isNumber(self, s: str) -> bool:
        """
        checks whether it is a valid number or not
        """
        if s.isalpha() or (s.isalnum() and (s[0] =='e' or s[0] == 'E')):
            return False
        elif self.isinteger(s) or self.isdecimal(s):
            return True 
        else:
            if "e" in s:
                e_index = s.index("e")
                if e_index == len(s) - 1:
                    return False
                elif e_index == 0:
                    return False
                else:
                    return self.isinteger(s[e_index + 1:])
            elif "E" in s:
                e_index = s.index("E")
                if e_index == len(s) - 1:
                    return False
                elif e_index == 0:
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
                
