class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0
        for t_pos in range(len(t)):
            if s_pos <= len(s) - 1 and t[t_pos] == s[s_pos]:
                s_pos += 1
        return s_pos == len(s)

# approach 2：
