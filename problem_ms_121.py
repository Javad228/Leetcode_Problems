class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = max(prices)
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] <min_price:
                min_price = prices[i]
            else:
                max_profit = max(prices[i] - min_price,max_profit)

        return max_profit

        
sol = Solution()
sol.maxProfit([7,1,5,3,6,4])