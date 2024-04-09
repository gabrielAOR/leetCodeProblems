# Problem link: https://leetcode.com/problems/valid-anagram/description/
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): 
            return False

        dictS, dictT = {}, {}

        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        for key in dictS:
            if dictS[key] != dictT.get(key, 0): 
                return False

        return True