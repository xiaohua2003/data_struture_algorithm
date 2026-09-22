class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set("aeiou")
        cur_count = sum(s[i] in vowel for i in range(k))
        res = cur_count
        for i in range(k, len(s)):
            if s[i] in vowel:
                cur_count += 1
            if s[i - k] in vowel:
                cur_count -= 1
            res = max(res, cur_count)
        return res
    
            
            


        