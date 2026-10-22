class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = [0] * 26
        t_lst = [0] * 26

        for i in s:
            idx = ord(i) - ord('a')
            s_lst[idx] += 1

        for i in t:
            idx = ord(i) - ord('a')
            t_lst[idx] += 1
        
        return s_lst == t_lst