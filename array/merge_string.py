# approach one
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        res = []
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])
        if n1 > n:
            res.append(word1[n:])
        if n2 > n:
            res.append(word2[n:])
        return "".join(res)

        