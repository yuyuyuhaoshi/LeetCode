class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}
        for char in s:
            # print(char)
            if char not in dict:
                # 如果char 是 ( [ {
                print('append:{}'.format(char))
                stack.append(char)
            else:
                if not stack:
                    return False 
                ch = stack.pop()
                print('pop:{}'.format(ch))
                if ch != dict[char]:
                    return False
        return not stack

if __name__ == "__main__":
    s = Solution()
    print(s.isValid('(]'))