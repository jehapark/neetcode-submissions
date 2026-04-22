class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid   

            if nums[mid] >= nums[l]:
                if target > nums[mid] or nums[l] > target:
                    l = mid + 1
                else: # target is less than middle and greater than left
                    r = mid - 1
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1
                else: # target is greater than middle and less than right
                    l = mid  + 1
        
        return -1
