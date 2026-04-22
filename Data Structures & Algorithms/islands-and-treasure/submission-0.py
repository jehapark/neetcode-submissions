class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == -1 or (r, c) in visited):
                return
            q.append([r, c])
            visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            distance += 1
