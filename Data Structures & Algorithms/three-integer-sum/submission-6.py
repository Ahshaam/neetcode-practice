class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = []

        for i in range(len(nums)):
            if nums[i] in used:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                    while nums[r+1] == nums[r] and l < r:
                        r-=1
            used.append(nums[i])

        return res
