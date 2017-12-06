class Solution(object):
    def twoSum(self, nums, target):
        # 输入一个list和一个变量
        # 当list中的某两个数值相加 = 变量时，
        # 返回数值中的索引组成的list
        if len(nums) <= 1:
            return False
        temp_dic = {}
        length = len(nums)
        # 设置一个空的字典，保存target与list中的每一个数值的差
        # 在遍历过程中遇到等值，就返回现在的i与在list的value
        # 字典中是 差-下表
        for i in range(length):
            if nums[i] in temp_dic:
                return [temp_dic[nums[i]], i]
            else:
                temp_dic[target - nums[i]] = i


solution = Solution()
print(solution.twoSum([3, 2, 4], 5))
