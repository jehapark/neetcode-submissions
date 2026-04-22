class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}

        for letter in s:
            if letter not in hashs:
                hashs[letter] = 1
            else:
                hashs[letter] = hashs[letter] + 1
        
        for letter in t:
            if letter not in hasht:
                hasht[letter] = 1
            else:
                hasht[letter] = hasht[letter] + 1
        
        return hashs == hasht