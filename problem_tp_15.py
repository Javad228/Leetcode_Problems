class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i+1
            right = len(nums)-1
            while left<right:
                target = nums[i]
                if left == i:
                    left+=1
                if right==i:
                    right-=1

                if nums[left]+nums[right] == 0-target:
                    res.append([target, nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left]+nums[right] > 0-target:
                    right-=1
                else:
                    left+=1
        return res

    

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))