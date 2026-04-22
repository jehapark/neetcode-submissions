class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        longest = 0
        l, r = 0, 1
        
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest

        