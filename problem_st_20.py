class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= list(s)
        st = []
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                elif i == ")" and st[-1] == "(":
                    st.pop()
                elif i == "}" and st[-1] == "{":
                    st.pop()
                elif i == "]" and st[-1] == "[":
                    st.pop()
                else:
                    return False
        if len(st)>0:
            return False
        return True

sol = Solution()
sol.isValid("([])")