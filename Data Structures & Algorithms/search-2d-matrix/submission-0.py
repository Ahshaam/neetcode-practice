class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for row in matrix:
            for val in row:
                flat.append(val)

        l, r = 0, len(flat) - 1
        while l <= r:
            mid = (l + r) // 2

            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
