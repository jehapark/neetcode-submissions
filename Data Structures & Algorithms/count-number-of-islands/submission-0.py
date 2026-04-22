class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in dirs:
                    r, c = row + dr, col + dc            
                
                    if (r in range(rows) and 
                        c in range(cols) and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        q.append((r, c))
                        visited.add((r, c))
                    
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1

        return islands
