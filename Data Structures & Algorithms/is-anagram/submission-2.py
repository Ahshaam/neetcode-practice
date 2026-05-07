from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = defaultdict(int)
        w2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            w1[s[i]] += 1
            w2[t[i]] += 1

        return w1 == w2