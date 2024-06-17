class Solution(object):
    def repeatedSubstringPattern(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        r = s
        for i in range(len(s)/2):
            r = r[1:] + r[0]
            if r == s:
                return True
        return False

        