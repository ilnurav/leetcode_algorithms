# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1
        
        num *= sign
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num
