class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # if > then update output & pop those lesser... in while loop
            while stack and t > stack[-1][1]: # if new temp is greater than a prev temp (the lowest)
                # update output for prev temp, pop it -- then repeat until new temp <
                prevIndex, prevVal = stack.pop()
                output[prevIndex] = i - prevIndex
            # then append either way
            stack.append([i, t])
        return output