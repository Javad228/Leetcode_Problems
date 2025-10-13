class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.rec(s, 0,4)

    def rec(self, s, last_idx, n):
        for i in range(last_idx,len(s)):
            if s[i] != '.' and int(s[i]) < 255:
                if n!=0:
                    self.rec(s[:i+1]+"."+ s[i+1:], i+1, n-1)
                self.rec(s, i, n)


        
        

sol = Solution()
sol.restoreIpAddresses("25525511135")