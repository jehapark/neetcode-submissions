class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # lower bound of monke eating banana per hour
        r = max(piles) # upper bound of monke eating is max banana pile (takes h hours)
        res = r

        while l <= r:
            mid = (l + r) // 2
            total = 0

            for p in piles:
                total += math.ceil(float(p) / mid)

            if total <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
            
        

