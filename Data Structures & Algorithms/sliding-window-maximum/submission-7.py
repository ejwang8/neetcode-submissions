class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # gonna use a deque where front i=0 is window max, i=-1 is lowest
        # keep track of indices
        # before add new elem, pop off all lower items then add
        # then remove stale items from the front

        # note to self: pop/append=right... popleft/appendleft=left

        maxes = []
        window_deque = collections.deque()
        l = r = 0

        for r in range(len(nums)):
            l = max(0, r-k+1)
            # print(l, r)
            while window_deque and nums[r] > nums[window_deque[-1]]: # pop smaller VALUES (in nums)
                window_deque.pop()
            window_deque.append(r)

            while window_deque and l > window_deque[0]: # check iNDICES
                window_deque.popleft()

            if window_deque and r >= k-1: # if have reached k window
                maxes.append(nums[window_deque[0]])

        return maxes