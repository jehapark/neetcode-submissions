class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break

        if not (l <= r):
            return False

        l2, r2 = 0, len(matrix[0]) - 1

        while l2 <= r2:
            mid2 = (l2 + r2) // 2
            if matrix[mid][mid2] > target:
                r2 = mid2 - 1
            elif matrix[mid][mid2] < target:
                l2 = mid2 + 1
            else:
                return True
        return False