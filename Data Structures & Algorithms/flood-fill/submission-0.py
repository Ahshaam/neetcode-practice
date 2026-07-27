class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        k = image[sr][sc]
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] != k or grid[r][c] == color):
                return 
            else:
                image[r][c] = color
            
            visit.add((r,c))
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)

        dfs(image, sr, sc, set())
        return image

            