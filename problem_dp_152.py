class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[]
        dp = nums[:]
        min_dp=[]
        min_dp = nums[:]

        for i in range(1,len(nums)):
            min_dp[i] = min(min_dp[i-1]*nums[i], nums[i],dp[i-1]*nums[i])
            dp[i] = max(dp[i-1]*nums[i], nums[i],min_dp[i-1]*nums[i])

        return max(max(min_dp),max(dp))
sol = Solution()
print(sol.maxProduct([2,-5,-2,-4,3]))