class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        removeCount = 0
        currEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= currEnd:
                currEnd = end
            else:
                removeCount += 1
        return removeCount