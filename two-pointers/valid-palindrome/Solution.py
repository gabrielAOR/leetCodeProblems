class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum, str(s)))
        s = s.lower()
        print(s)
        j = -1
        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j -= 1
        return True