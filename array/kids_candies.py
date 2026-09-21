class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        res = [False] * len(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candies:
                res[i] = True
        return res
        