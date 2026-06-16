class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unq = set(nums)
        cnt = 0
        res = 0
        
        for i in unq:
            if i - 1 in unq:
                continue

            cnt = 1
            while i + 1 in unq:
                cnt += 1
                i += 1

            res = max(cnt, res)
        
        return res
