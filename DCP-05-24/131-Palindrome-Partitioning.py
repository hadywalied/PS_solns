class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        partitions = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if is_palindrom(prefix):
                for suffix in self.partition(s[i:]):
                    partitions.append([prefix] + suffix)
        return partitions


def partition_string(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]

def is_palindrom(s):
    return s == s[::-1]        