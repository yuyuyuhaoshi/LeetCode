class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            s = s[::-1][:-1]  # 去掉末尾的-
            return -int(s) if int(s) < 2 ** 31 else 0
        else:
            s = s[::-1]
            return int(s) if int(s) < 2 ** 31 - 1 else 0


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = int(line);

            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
