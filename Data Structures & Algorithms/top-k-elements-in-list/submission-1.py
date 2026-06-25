class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, count in count.items():
            frequency[count].append(num)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for val in frequency[i]:
                res.append(val)
                if len(res) == k:
                    return res
