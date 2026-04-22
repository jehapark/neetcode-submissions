class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                count = 0
                while (num + count) in numSet:
                    count += 1
                largest = max(largest, count)
            else:
                continue

        return largest
                