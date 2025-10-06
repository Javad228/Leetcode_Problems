class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashy = {}
        for i in range(len(nums)):
            hashy[nums[i]] = i
        
        for i in range(len(nums)):
            if (target-nums[i]) in hashy and  hashy.get(target-nums[i]) != i:
                return [i, hashy.get(target-nums[i])]
        
sol = Solution()
sol.twoSum([2,7,11,15],9)