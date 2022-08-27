def isPalindrome(self, s: str) -> bool:
    """
    https://leetcode.com/problems/valid-palindrome/
    
    Easy: 125. Valid Palindrome
    """
    ss = ''
    for i in s:
        if i.isalnum():
            ss = ss + i
    # ss is the lower case without any spaces
    ss = ss.lower()
    # to check whether or not it is a pallindrome
    return ss == ss[len(ss) :: -1]
        
