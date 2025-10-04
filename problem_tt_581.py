class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted = nums[:]
        sorted.sort()
        start = 0
        end = 0
        f =0
        for i in range(len(nums)):
            if nums[i] != sorted[i] and f==0:
                start = i
                f= 1
            elif nums[i] != sorted[i] and f==1:
                end = i
        ret = 0
        if (end-start) != 0:
            ret = end-start+1
        return ret
    
sol = Solution()
print(sol.findUnsortedSubarray([1,3,2,2,2]))
print(sol.findUnsortedSubarray([1,3,2,3,3]))
print(sol.findUnsortedSubarray([2,3,3,2,4]))
print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))

