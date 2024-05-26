class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        x = list(word1)
        y = list(word2)
        result = []
        while x or y:
            try:
                t = x.pop(0)
            except:
                t = None
            try:
                u = y.pop(0)
            except:
                u = None
            if t:
                result.append(t)
            if u:
                result.append(u)
        return ''.join(result)

        