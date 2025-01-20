# https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
