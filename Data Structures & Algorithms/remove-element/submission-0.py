class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n != val:
                nums[k] = n
                k += 1
            if n == val:
                nums[i] = 0
        
        return k
        

            
