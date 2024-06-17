class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # create a dictionary to store the frequency of each letter in s
        freq = {}
        for letter in s:
            if letter not in freq:
                freq[letter] = 0
            freq[letter] += 1
        print(freq)
        freq2 = {}
        for letter in t:
            if letter not in freq2:
                freq2[letter] = 0
            freq2[letter] += 1
        print(freq2)
        # region Calculate the difference between the frequencies of s and t
        diff_freq = {}
        for letter, count in freq2.items():
            if letter not in freq or count != freq[letter]:
                return letter
        # endregion
        return None