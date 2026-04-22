class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(set(nums)) == 1:
            return [nums[0]]
        
        hash = {}

        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1

        count = [[] for x in range(len(nums) + 1)]

        for n, c in hash.items():
            count[c].append(n)
        
        topk = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                topk.append(n)
                if len(topk) == k:
                    return topk



        

        
