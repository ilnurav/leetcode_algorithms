# https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
