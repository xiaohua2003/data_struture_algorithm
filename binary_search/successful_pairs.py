class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        res = []
        for spell in spells:
            l = 0
            r = len(potions)
            while l < r:
                mid = (l + r) // 2
                if potions[mid] * spell < success:
                    l = mid + 1
                elif potions[mid] * spell >= success:
                    r = mid
            res.append(len(potions) - l)
        return res
# n = len(spells), m = len(potions)
# running time: O(n * log m) + o(m * log m)
# space complexitiy: O(n + m)
      



        