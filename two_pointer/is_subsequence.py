class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0
        for t_pos in range(len(t)):
            if s_pos <= len(s) - 1 and t[t_pos] == s[s_pos]:
                s_pos += 1
        return s_pos == len(s)

# approach 2：
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)
     

         