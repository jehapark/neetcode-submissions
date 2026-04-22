class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(curr, incurr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not incurr[i]:
                    curr.append(nums[i])
                    incurr[i] = True
                    dfs(curr, incurr)
                    curr.pop()
                    incurr[i] = False
        
        dfs([], [False] * len(nums))
        return res
            