class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1:
            return [nums]

        ret = self.permute(nums[1:])
        f_ret = []
        for arr in ret:
            for i in range(len(arr)+1):
                cop = arr.copy()
                cop.insert(i,nums[0])
                f_ret.append(cop)
                
        return f_ret


sol = Solution()
print(sol.permute([1,2,3]))
