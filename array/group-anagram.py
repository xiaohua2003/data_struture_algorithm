from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            strs_map[key].append(s)
        return list(strs_map.values())
       
            


        