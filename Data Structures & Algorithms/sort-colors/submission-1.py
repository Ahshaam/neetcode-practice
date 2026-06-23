class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bckt = [0, 0, 0]

        for i in nums:
            bckt[i] += 1
        
        i = 0
        for n in range(len(bckt)):
            for _ in range(bckt[n]):
                nums[i] = n
                i += 1
        
        return nums
