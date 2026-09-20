# approach 1
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval:interval[0])
        res = []
        n = len(intervals)
        if n <= 1:
            return intervals
        cur_end = sorted_intervals[0][1]
        cur_start = sorted_intervals[0][0]
        for i in range(1, n):
            if sorted_intervals[i][0] <= cur_end:
                cur_end = max(cur_end, sorted_intervals[i][1])
            else:
                res.append([cur_start, cur_end])
                cur_start = sorted_intervals[i][0]
                cur_end = sorted_intervals[i][1]
        res.append([cur_start, cur_end])
        return res
# appraoch 2
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]
        sorted_intervals = sorted(intervals, key=lambda interval:interval[0])
        res = []
        for start, end in sorted_intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
     

            


        
            


        