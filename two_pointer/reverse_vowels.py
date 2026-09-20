class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = set("aeiouAEIOU")
        l = 0
        r = n - 1
        s_list = list(s)
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        return "".join(s_list)
            
 
        

            



        