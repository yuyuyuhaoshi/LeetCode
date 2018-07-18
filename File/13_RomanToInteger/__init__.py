class Solution:
    def __init__(self):
        self.romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        p = 'I'
        s = s[::-1]  # 逆序
        for i in s:
            res = res - self.romans[i] if self.romans[i] < self.romans[p] else res + self.romans[i]
            p = i  # 交换
        
        return res
