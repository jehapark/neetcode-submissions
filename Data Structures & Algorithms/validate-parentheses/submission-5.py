class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for char in s:
            if char in closeToOpen and stack:
                if closeToOpen[char] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False
