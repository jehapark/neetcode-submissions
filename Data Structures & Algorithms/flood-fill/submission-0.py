class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src = image[sr][sc]
        if color == src:
            return image

        rows, cols = len(image), len(image[0])
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == src:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image
            