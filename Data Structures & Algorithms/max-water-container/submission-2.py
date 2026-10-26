class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            left = heights[l]
            right = heights[r]
            area = min(left, right) * (r - l)
            max_area = max(max_area, area)

            if left < right:
                l += 1
            else:
                r -= 1
        
        return max_area

