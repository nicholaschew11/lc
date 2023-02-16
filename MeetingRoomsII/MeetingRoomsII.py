class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)
        ans, temp, s, e = 0, 0, 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                temp += 1
                s += 1
            else:
                temp -= 1
                e += 1
            ans = max(ans, temp)
        return ans