class Solution:
    def mySqrt(self, x):
        import math
        """
        :type x: int
        :rtype: int
        """
        sqr = math.sqrt(x)
        sqr = math.floor(sqr)
        return sqr


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))
