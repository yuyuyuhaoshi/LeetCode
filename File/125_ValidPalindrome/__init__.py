class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1 or len(s) == 0:
            return True
        s = Solution.remove_punctuation(s)
        reversed_s = s[::-1]
        for i in range(len(s)):
            if s[i] != reversed_s[i]:
                return False
        return True

    @staticmethod
    def remove_punctuation(line):
        import re
        rule = re.compile(r'[^a-zA-Z0-9]')
        line = rule.sub('',line)
        return line.upper()

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(' '))