from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        word1_freq = sorted(word1_count.values())
        word2_freq = sorted(word2_count.values())
        if word1_count.keys() == word2_count.keys() and word1_freq == word2_freq:
            return True
        else:
            return False
        