class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binary serach on k to return between 1 and max value in piles (m = max(piles))
        # O(n * log(m))
        # binary search on k ...
        # within that loop through 1-p in piles to count up hours and see if it works
        l, r = 1, max(piles)
        minimum = r

        while l <= r: # 1, 4

            k = (l + r) // 2 # 2 --> 1

            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # 1 + 2 + 2 + 1 = 6

            if hours <= h:
                minimum = k # 6
                r = k - 1 # 1

            else:
                l = k + 1
        
        return minimum
