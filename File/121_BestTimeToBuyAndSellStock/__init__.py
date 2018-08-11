class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, min_price = 0, float('inf') 
        for price in prices:
            min_price = min(min_price, price) 
            profit = max(profit, price - min_price)
        return profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))