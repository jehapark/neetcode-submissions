class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair of elements (index, height)
        maxArea = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # if next height is less than the prev height:
                maxArea = max(maxArea, stack[-1][1] * (i - stack[-1][0]))
                start = stack[-1][0]
                stack.pop()
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
            # you shouldn't pop here since we lose values to iterate to (potential max areas) then

        return maxArea
