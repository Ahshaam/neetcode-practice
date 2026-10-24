class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cur = 1
                nxt = num + 1
                while nxt in nums:
                    cur += 1
                    nxt += 1
                longest = max(longest, cur)
        
        return longest
