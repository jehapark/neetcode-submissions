class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        index = 0
        for num in nums:
            if (target - num) in hash:
                return [hash[target - num], index]
            else:
                hash[num] = index
                index += 1
