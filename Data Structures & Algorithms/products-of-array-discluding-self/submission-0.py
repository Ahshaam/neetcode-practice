class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # p = []
        # for j in range(len(nums)):
        #     for i, n in enumerate(nums):
        #         if i != j:
        #             prod *= n
        #     p.append(prod)
        #     prod = 1
        # return p

        # n = len(nums)
        # p = [0] * (n + 1)
        # p[0] = 1

        # res = [0] * n
        # for i in range(n):
        #     p[i+1] = p[i] * nums[i]  

        # for i in range(1, n+1):
        #     l = p[i-1]
        #     r = p[n] // p[i]
        #     res[i-1] = l * r
        # return res

        n = len(nums)
        
        prefix = [1] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]

        res = [0] * n
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] = prefix[i] * suffix
            suffix *= nums[i]

        return res