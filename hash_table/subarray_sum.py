from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        prefix_sum = 0
        freq[0] = 1
        res = 0
        for num in nums:
            prefix_sum += num
            previous_sum = prefix_sum - k
            res += freq[previous_sum]
            freq[prefix_sum] += 1
        return res

        
            

    

        