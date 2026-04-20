class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        n = len(numbers)

        while i < n:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            j += 1

            if j >= n:
                j = 0
                i += 1