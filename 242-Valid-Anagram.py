class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq1 = {char: s.count(char) for char in set(s)}
        freq2 = {char: t.count(char) for char in set(t)}
        return len(s) == len(t) and all([True if ch in freq2 and count == freq2[ch] else False for ch, count in freq1.items()])
        