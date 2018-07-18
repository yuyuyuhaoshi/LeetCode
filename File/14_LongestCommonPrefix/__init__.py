class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        for index, letter in enumerate(shortest_str):
            for other_str in strs:
                if other_str[index] != letter:
                    return other_str[:index]
        return shortest_str


if __name__ == "__main__":
    solution = Solution()
    solution.longestCommonPrefix(["12", "12", "123"])