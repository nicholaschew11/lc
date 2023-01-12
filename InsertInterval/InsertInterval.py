class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        added = False

        for curr in intervals:
            if newInterval[0] > curr[1]:
                ans.append(curr)

            elif newInterval[1] < curr[0]:
                if not added:
                    ans.append(newInterval)
                    added = True
            
                ans.append(curr)

            else:
                newInterval[0] = min(curr[0], newInterval[0])
                newInterval[1] = max(curr[1], newInterval[1])

        if not added:
            ans.append(newInterval)

        return ans