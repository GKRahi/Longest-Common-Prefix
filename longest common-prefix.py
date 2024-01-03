class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        
        strs.sort()

        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix)!=0:
               prefix = prefix[:-1]
            
        return prefix
