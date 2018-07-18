class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        revert_str_x = str_x[::-1]
        for raw, revert in zip(str_x, revert_str_x):
            if raw != revert:
                return False
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    x = solution.isPalindrome(-121)
    print(x)