class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n - 1
        res = 0
        while l < r:
            cur_sum  = nums[l] + nums[r]
            if cur_sum == k:
                res += 1
                l += 1
                r -= 1
            elif cur_sum < k:
                l += 1
            else: 
                r -= 1
        return res
        