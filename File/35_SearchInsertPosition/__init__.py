class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 7))