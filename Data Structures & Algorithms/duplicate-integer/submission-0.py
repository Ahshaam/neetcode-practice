class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        counts = {}
        for i in range(n):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
        for i in counts:
            if counts[i] > 1:
                return True
        return False
