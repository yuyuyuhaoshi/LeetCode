class Solution:
    def generate(self, numRows):
        import copy
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1],]
        for i in range(1, numRows):
            new_array = []
            zero = [0]
            zero.extend(res[i-1])
            a = copy.deepcopy(zero) 
            b = copy.deepcopy(res[i-1])
            b.append(0)
            for j, k in zip(a, b):
                new_array.append(j+k)
            res.append(new_array)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
        