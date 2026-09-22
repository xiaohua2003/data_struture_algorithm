class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        cur_altitude = 0
        highest = 0
        for val in gain:
            cur_altitude += val
            highest = max(highest, cur_altitude)
        return highest
        