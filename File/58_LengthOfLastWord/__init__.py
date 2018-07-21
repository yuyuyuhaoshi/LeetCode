class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        words = s.rstrip(' ').split(' ')
        return len(words[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))