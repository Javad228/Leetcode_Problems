class Solution(object):
    def expand(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        
        def backtrack(idx,build=""):
            if idx>=len(s):
                ret.append(build)
                return

            if s[idx] == "{":
                end_idx = s.find("}",idx)
                arr = s[idx+1:end_idx].split(',')
                for i in arr:
                    backtrack(end_idx+1,build+i)
            else:
                backtrack(idx+1,build+s[idx])
            
        backtrack(0,"")
        ret.sort()
        return ret