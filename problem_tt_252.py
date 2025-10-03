class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals)<2:
            return True
        intervals.sort()
        last = intervals[0]
        for interval in intervals[1:]:
            if last[1]>interval[0]:
                return False
            last = interval

        return True
        