class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        cur_prefix = 0
        for i in range(n):
            prefix_sum[i] = cur_prefix
            cur_prefix += nums[i]
        suffix_sum = [0] * n
        cur_suffix = 0
        for j in range(n - 1, -1, -1):
            suffix_sum[j] = cur_suffix
            cur_suffix  += nums[j]
        
        for z in range(n):
            if prefix_sum[z] == suffix_sum[z]:
                return z
        return -1

            
# appraoch two
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if right_sum == left_sum:
                return i
            left_sum += num
        return -1


            


        

        