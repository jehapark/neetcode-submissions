class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum, res = 0, float("infinity")
        l = 0 

        for r in range(len(nums)):
            currsum += nums[r]

            while currsum >= target:
                res = min(res, r - l + 1)
                currsum -= nums[l]
                l += 1
        
        return res if res != float("infinity") else 0