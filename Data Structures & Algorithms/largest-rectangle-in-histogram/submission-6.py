class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        streaks = [] #[(index, height), (…)] going from left to right
        
        for index, height in enumerate(heights):
            extend_back_start = index
            while streaks and height < streaks[-1][1]:
                #pop
                lastIndex, lastHeight = streaks.pop()
                maxArea = max(maxArea, lastHeight * (index - lastIndex))
                # streaks.append((lastIndex, height))
                extend_back_start = lastIndex

            streaks.append((extend_back_start, height))

        #At end must try out remaining streaks
        print(streaks)
        for index, height in streaks:
            maxArea = max(maxArea, height * (len(heights)-index))
            # print(maxArea)

        return maxArea