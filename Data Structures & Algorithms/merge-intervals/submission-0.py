class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for start, end in intervals:
            currEnd = res[-1][1]
            if start <= currEnd:
                res[-1][1] = max(currEnd, end)
            else:
                res.append([start, end])
        
        return res