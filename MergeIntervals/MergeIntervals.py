class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda x: x[0])
        c = 0
        for i in range(1, len(intervals)):
            if intervals[c][1] < intervals[i][0]:
                ans.append(intervals[c])
                c = i
            else:
                intervals[c][1] = max(intervals[c][1], intervals[i][1])
        ans.append(intervals[c])
        return ans