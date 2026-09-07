class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        counts = defaultdict(int)

        l = 0
        for r in range(len(s)):
            # print('l,r', l, r)
            counts[s[r]] += 1

            # length is r - l + 1
            while (r-l+1) - max(counts.values(), default=0) > k: # IF NOT VALID, MOVE L
                counts[s[l]] -= 1
                l +=1

            res = max(res, r-l+1) # update
            # print(res) #AAABABB
            

        return res

        