class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # In case the string consist of only single letters or an empty string
        if len(s) < 2:
            return len(s)
        else:
            l = []
            index = 0
            max_length = 0

            while index < len(s) - 1:
                substring = ""
                substring = substring + s[index]

                while index < len(s) and s[index] not in substring:
                    substring = substring + s[index]

                l.append(substring)
                max_length = max(max_length, len(substring))
            return max_length
