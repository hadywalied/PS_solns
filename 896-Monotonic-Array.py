class Solution(object):
    def isMonotonic(self, l):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(l) <= 1:
            return True
        if l[0] > l[1]:
            return all(l[i] >= l[i+1] for i in range(len(l) - 1))
        elif l[0] < l[1] : 
            return all(l[i] <= l[i+1] for i in range(len(l) - 1))
        else:
            return all(l[i] <= l[i+1] for i in range(len(l) - 1)) or all(l[i] >= l[i+1] for i in range(len(l) - 1))
   