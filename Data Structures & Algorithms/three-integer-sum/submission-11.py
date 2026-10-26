class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = num + sorted_nums[l] + sorted_nums[r]
                if cur < 0:
                    l += 1
                elif cur > 0:
                    r -= 1
                else:
                    res.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
        return res
            