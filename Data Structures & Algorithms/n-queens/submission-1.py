class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiag, negDiag = set(), set(), set()
        
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (c - r) in negDiag or (c + r) in posDiag:
                    continue
                
                cols.add(c)
                posDiag.add(c + r)
                negDiag.add(c - r)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(c + r)
                negDiag.remove(c - r)
                board[r][c] = "."
        
        backtrack(0)
        return res