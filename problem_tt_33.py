class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0]==target: 
            return 0
        
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid]>=nums[left]: #left hand of mid is sorted
                if nums[left]<=target and target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else: #right hand of mid is sorted
                if nums[right]>=target and target >= nums[mid]:
                    left = mid+1
                else:
                    right = mid-1


        
        return -1

        
sol = Solution()
print(sol.search([3,1],3))