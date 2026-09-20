class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
        prev_end = sorted_intervals[0][1]
        res = 0
        for start, end in sorted_intervals[1:]:
            if prev_end > start:
                res += 1
            else:
                prev_end = end
        return res

      
