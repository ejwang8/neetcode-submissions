class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3: return 0
        
        # make prefix and suffix max
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        prefix[1] = height[0]
        n = len(height)

        for l in range(2, n):
            prefix[l] = max(height[l-1], prefix[l-1])

        suffix[n-2] = height[n-1]
        for r in range(n-3, -1, -1):
            suffix[r] = max(height[r+1], suffix[r+1])
        
        sum = 0

        # print(prefix)
        # print(suffix)

        for i in range(n):
            sum += max(0, min(prefix[i], suffix[i]) - height[i])

        return sum