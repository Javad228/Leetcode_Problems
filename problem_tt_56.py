class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==1:
            return intervals
        intervals.sort()
        compare = intervals[0]
        ret = []
        for interval in intervals[1:]:
            if compare[1] >= interval[0]:
                compare[1] = max(compare[1], interval[1])
            else:
                ret.append(compare)
                compare = interval
        ret.append(compare)
        return ret
        
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))