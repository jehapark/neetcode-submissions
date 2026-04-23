class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case if t is empty
        if t == "": return ""
        hash1, hash2 = {}, {}
        
        for char in t:
            hash1[char] = 1 + hash1.get(char, 0)

        have, need = 0, len(hash1)
        minindex, minlen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            hash2[c] = 1 + hash2.get(c, 0)

            if c in hash1 and hash1[c] == hash2[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < minlen:
                    minindex = [l, r]
                    minlen = min(r - l + 1, minlen)
                
                hash2[s[l]] -= 1

                if s[l] in hash1 and hash2[s[l]] < hash1[s[l]]:
                    have -= 1

                l += 1

        l, r = minindex
        return s[l:r + 1] if minlen != float("infinity") else ""

                

    