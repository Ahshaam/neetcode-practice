from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = [0] * 26
        cnt_t = [0] * 26

        for i in s:
            idx = ord(i) - ord('a')
            cnt_s[idx] += 1
        
        for i in t:
            idx = ord(i) - ord('a')
            cnt_t[idx] += 1
        
        return cnt_s == cnt_t