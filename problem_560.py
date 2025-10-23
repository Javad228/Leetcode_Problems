class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        cnt = 0
        ret = 0
        freq[0] = 1
        for i in nums:
            cnt+=i
            ret += freq.get(cnt-k,0)
            freq[cnt] = freq.get(cnt,0) +1


            
        return ret

        
