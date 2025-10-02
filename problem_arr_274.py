class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        ans = 0
        if max(citations) > 0 : 
            ans =1
            
        for i in range(len(citations)):
            if citations[i]!=0:
                # amount left in arr >= current citation numb
                leftover = len(citations)-i
                if leftover>=citations[i]: 
                    ans = citations[i]
                else:
                    ans = max(ans,leftover)

        return ans

        
sol = Solution()
print(sol.hIndex([3,0,6,1,5]))
print(sol.hIndex([11, 15]))
print(sol.hIndex([1,3,1]))
print(sol.hIndex([0,0,2]))
0,1,3,5,6
0,0,2
