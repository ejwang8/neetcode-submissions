class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLen = 0
        l = 0
        charSet = set()

        for r in range(len(s)):#4,6 / {x,y,z} / 3
            #s[r] / s[l]

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])

            maxLen = max(maxLen, r-l+1)
        return maxLen