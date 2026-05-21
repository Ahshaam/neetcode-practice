class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_cnt = 0
        for i in nums:
            if i != 1:
                count = 0 
            else:
                count += 1
            if count > max_cnt:
                max_cnt = count

        return max_cnt

        