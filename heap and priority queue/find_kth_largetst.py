class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k
        def quickSelect(arr, target):
            mid = len(arr) // 2
            pivot = arr[mid]
            lows = [num for num in arr if num < pivot]
            mids = [num for num in arr if num == pivot]
            highs = [num for num in arr if num > pivot]
            if target < len(lows):
                return quickSelect(lows, target)
            elif target < len(arr) - len(highs):
                return pivot
            else:
                return quickSelect(highs, target - len(lows) - len(mids))
        return quickSelect(nums, target)

      # Time:  O(n) expected with randomized pivot, T(n) = T(n/2) + n which will be O(n). O(n^2) worst because T(n) = T(n - 1) + n
      # Space: O(n) for balanced partitions: n + n/2 + n/4 + n/8 + ... = O(n), O(n^2) worst: n + (n - 1) + (n - 2) + ... + 1 = O(n ^ 2)
        
       



        
        