class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        cur = 1
        for i in range(len(nums)):
            prefix[i] = cur
            cur *= nums[i]
        
        suffix = [0] * len(nums)
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = cur
            cur *= nums[i]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res