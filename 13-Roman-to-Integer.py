class Solution(object):
    def romanToInt(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        table = {
            \I\: 1,
            \V\: 5,
            \X\: 10,
            \L\: 50,
            \C\: 100,
            \D\: 500,
            \M\: 1000,
        }
        sum = 0
        i=-1
        for i in range(len(s)-1):
            if table[s[i]] >= table[s[i+1]]:
                sum += table[s[i]]
            else:
                sum -= table[s[i]]
        sum+=table[s[i+1]]
        return sum