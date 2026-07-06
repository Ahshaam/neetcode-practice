class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chrs = set()
        m = 0
        for r in range(len(s)):
            while s[r] in chrs:
                chrs.remove(s[l])
                l += 1
            m = max(m, r - l + 1)
            chrs.add(s[r])

        return m
            