from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1
        freq_lists = freq.values()
        freq_sets = set(freq_lists)
        return len(freq_lists) == len(freq_sets)
        