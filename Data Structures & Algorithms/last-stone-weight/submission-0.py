class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
            
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if second > first:
                heapq.heappush(maxHeap, first - second)
        
        maxHeap.append(0)
        return abs(maxHeap[0])