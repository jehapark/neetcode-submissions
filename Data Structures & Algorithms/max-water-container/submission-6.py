class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1
        maxl, maxr = heights[l], heights[r]

        while l < r:
            res = max(res, min(maxl, maxr) * (r - l))
            if maxl >= maxr:
                r -= 1
                maxr = max(maxr, heights[r])
            else:
                l += 1
                maxl = max(maxl, heights[l])
        
        return res

