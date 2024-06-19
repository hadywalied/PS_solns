class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr, reverse=True)
        v1 = arr[0]
        v2 = arr[1]
        diff = v1 - v2
        for elem in arr[2:]:
            diff2 = v2 - elem
            if diff2 != diff:
                return False
            v2 = elem
            
        return True
        
