class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        n = len(s)
        seen = set()
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            count = max(count, i - l + 1)
        return count


 

     


     


       
      

          
            

            
    


      


      

       

       


        