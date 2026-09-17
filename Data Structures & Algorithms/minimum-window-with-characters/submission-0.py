class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t): return ""  

        # ???
        from collections import defaultdict

        # make two hash maps for s and t (s is longer, t is shorter)
        shortHash, longHash = defaultdict(int), defaultdict(int)

        # go through t and establish t's hash map values
        for ch in t:
            shortHash[ch] += 1

        # initialize res, resLen
        resIndices, resLen = [-1, -1], float("inf")

        # iterate with l, r... r moves through s
            # update s's hashmap each letter
                # keep track of have vs. need... update that
            # THEN while have == need
                # pop off the left
                    # update the s hashmap
                    # each time update res and resLen
                    # decrement have if meet conditions

        l = 0
        have, need = 0, len(shortHash)

        for r in range(len(s)):
            ch_r = s[r]
            longHash[ch_r] += 1
            if (longHash[ch_r] == shortHash[ch_r]): have += 1

            while have == need:
                # update res and resLen
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    resIndices = [l, r]

                ch_l = s[l]
                longHash[ch_l] -= 1
                l += 1
                if longHash[ch_l] == shortHash[ch_l] - 1: have -= 1
        if resLen == float("inf"): return ""
        else: return s[resIndices[0]:resIndices[1]+1]

        