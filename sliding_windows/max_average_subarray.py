class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        res = cur_sum
        n = len(nums)
        for i in range(1, n - k + 1):
            cur_sum += nums[i + k - 1]
            cur_sum -= nums[i - 1]
            res = max(res, cur_sum)
        return res / k

# approach 2


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        res = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            res = max(res, cur_sum)
        return res / k
   
        

      
            
        
      
            
        