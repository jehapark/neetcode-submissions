class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            for n in range(i, len(candidates)):
                if n > i and candidates[n] == candidates[n - 1]:
                    continue
                if total + candidates[n] > target:
                    break
                
                curr.append(candidates[n])
                dfs(n + 1, curr, total + candidates[n])
                curr.pop()

        dfs(0, [], 0)
        return res