class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        maxl, maxr = 0, 0

        while l < r:
            water = (r - l) * min(heights[r], heights[l])
            res = max(res, water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res

