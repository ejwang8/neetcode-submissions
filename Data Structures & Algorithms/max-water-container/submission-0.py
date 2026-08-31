class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # linear solution O(n)
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            y = min(heights[l], heights[r])
            x = r - l
            maxArea = max(maxArea, x*y)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
