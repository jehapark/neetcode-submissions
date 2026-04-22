class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time = 0
        numFresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    numFresh += 1
                if grid[row][col] == 2:
                    q.append([row, col])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and numFresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    numFresh -= 1
            time += 1
        return time if numFresh == 0 else -1