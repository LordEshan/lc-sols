class Solution(object):
    def longestCommonPrefix(self, strs):
        firstword = strs[0]             

        for word in strs:                                           
            while not word.startswith(firstword):           
                firstword = firstword[:-1]
                
                if firstword =="":
                    return ""
        return firstword