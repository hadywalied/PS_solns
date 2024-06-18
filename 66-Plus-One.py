class Solution(object):
    def plusOne(self, digits):
        \\\
        :type digits: List[int]
        :rtype: List[int]
        \\\
        result = []
        incr = False
        once = False
        while len(digits) > 0 or incr:
            if digits:
                d = digits.pop(-1)
                if d == 9 and not once:
                    result.insert(0, 0)
                    incr = True
                    continue
            if incr:
                if d == 9:
                    result.insert(0, 1)
                else:
                    if not once:
                        result.insert(0, d+1)
                        once = True
                    else:
                        result.insert(0, d)
                incr = False
            else:
                if not once:
                    result.insert(0, d+1)
                    once = True
                else:
                    result.insert(0, d)

        return result
