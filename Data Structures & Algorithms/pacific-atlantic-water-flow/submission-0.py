class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, ocean, prevHeight):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                (r, c) in ocean or 
                heights[r][c] < prevHeight):
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])
        
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in atl and (row, col) in pac:
                    res.append([row, col])
        
        return res


                    