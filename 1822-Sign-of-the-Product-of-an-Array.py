class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = False
        for x in nums:
            if x == 0:
                return 0
            if  x < 0:
                f= not f
        if f:
            return -1
        else:
            return 1    
        