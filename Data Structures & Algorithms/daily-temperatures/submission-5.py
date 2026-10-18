class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []


        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                temp_i, temp_t = stack.pop()
                res[temp_i] = i - temp_i
            stack.append((i, t))
        
        return res