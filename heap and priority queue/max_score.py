import heapq
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums_pair = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        max_val = 0
        heap = []
        total = 0

        for a, b in nums_pair:
            heapq.heappush(heap, a)
            total += a
            if len(heap) > k:
                removed = heapq.heappop(heap)
                total -= removed
            if len(heap) == k:
                max_val = max(max_val, total * b)
        return max_val

        # running time: O(n log n)
        # space complexity: O(n)
 

                

