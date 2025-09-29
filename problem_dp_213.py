class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = len(nums)-1
        if last<2:
            return max(nums)
        return max(self.hr(nums[:-1]),self.hr(nums[1:]))

    def hr(self,nums):
        dp = nums.copy()
        last = len(dp)-1
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            left = dp[i]+dp[i-2]
            right = dp[i-1]
            dp[i] = max(left,right)

        return dp[last]

sol = Solution()
print(sol.rob([1,3,1,3,100]))