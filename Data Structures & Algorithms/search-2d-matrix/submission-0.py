class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow = 0
        rrow = len(matrix) - 1

        lcol = 0
        rcol = len(matrix[0]) - 1

        while lrow <= rrow:
            midrow = (lrow + rrow) // 2

            if target > matrix[midrow][-1]:
                lrow = midrow + 1
            elif target < matrix[midrow][0]:
                rrow = midrow - 1
            else:
                break
        
        if not (lrow <= rrow):
            return False

        midrow = (lrow + rrow) // 2

        while lcol <= rcol:
            midcol = (lcol + rcol) // 2

            if target > matrix[midrow][midcol]:
                lcol = midcol + 1
            elif target < matrix[midrow][midcol]:
                rcol = midcol - 1
            else:
                return True
        
        return False

            
