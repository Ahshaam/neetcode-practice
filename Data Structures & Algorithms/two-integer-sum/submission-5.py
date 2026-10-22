class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()

        for i, n in enumerate(nums):
            dif = target - n

            if dif not in table:
                table[n] = i
            else:
                return [table[dif], i]
        
        return []