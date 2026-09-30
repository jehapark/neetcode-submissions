class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 1

        for i in range(1, 2 * len(nums)):
            if nums[(i - 1) % len(nums)] <= nums[i % len(nums)]:
                count += 1
            else:
                count = 1
            
            if count == len(nums):
                return True

        return len(nums) == 1