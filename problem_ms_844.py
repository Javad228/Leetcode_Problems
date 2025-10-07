class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st1=[]
        st2=[]
        for i in s:
            if i=='#' and len(st1)!=0:
                st1.pop()

            if i!='#':
                st1.append(i)
        
        for i in t:
            if i=='#' and len(st2)!=0:
                st2.pop()
            
            if i!='#':
                st2.append(i)
        
        return st1 == st2


sol = Solution()
print(sol.backspaceCompare("ab#c","ad#c"))