class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        max_num = 0
        maxFreq = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxFreq = max(maxFreq, counts[s[r]])
            while (r - l + 1) - maxFreq > k:
                counts[s[l]] -= 1
                l += 1
            max_num = max(max_num, r - l + 1)
        
        return max_num