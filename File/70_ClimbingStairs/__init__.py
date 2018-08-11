class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
            print("_: {}\ta: {}\tb: {}".format(_+1,a,b))
        return a

if __name__ == '__main__':
    s = Solution()
    s.climbStairs(10)