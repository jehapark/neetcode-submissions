class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz" }
        
        def backtrack(i, currSet):
            if len(currSet) == len(digits):
                res.append(currSet)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, currSet + c)
        
        if digits:
            backtrack(0, "")
        return res