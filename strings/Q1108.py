class Solution:
    def defangIPaddr(self, address: str) -> str:
      """
      https://leetcode.com/problems/defanging-an-ip-address/
      
      Given a valid (IPv4) IP address, return a defanged version of that IP address.

      A defanged IP address replaces every period "." with "[.]".
      """
        return address.replace('.', '[.]')
        
