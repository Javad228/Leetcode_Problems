class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashy = {}

        left = 0
        max_len=0
        s = list(s)
        while left<len(s):
            idx = hashy.get(s[left])
            if idx==None:
                hashy[s[left]] = left
                left+=1
            else:
                left = idx+1
                idx = None
                max_len=max(len(hashy),max_len)
                hashy = {}
        max_len=max(len(hashy),max_len)        
        return max_len
            
        
sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))