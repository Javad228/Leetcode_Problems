class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lop = []
        if s[0] == '0':
            return 0
        lop.append([s[0]])
        for i in range(1,len(s)):
            app = []
            for arr in lop:
                last= len(arr)-1
                if arr[last] != '0':
                    if int(arr[last]+s[i]) <= 26:
                        add = arr[:]
                        add[last] = arr[last]+s[i]
                        app.append(add)
                    if s[i]!= '0':
                        base = arr[:]
                        base.append(s[i])
                        app.append(base)
            lop = app[:]
        return len(lop)
                    
        
sol = Solution()
print(sol.numDecodings("06"))