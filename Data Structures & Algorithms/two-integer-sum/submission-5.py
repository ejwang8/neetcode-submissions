class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # EW ORIGINAL ANSWER WAS O(N^2) FREAK

        # nums=[1 3 5]; target = 6; i=0, j=2
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         if i == j: continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # O(n) attempt after watching soln video lol
        # hash map only seen values in list (avoids repeats) via dict {}
        seen = {}

        for i, n in enumerate(nums):
            # first check in dict if (target-nums[i]) is there
            # if there, return!
            # if not, add curr i, n to dict
            if (target - nums[i]) in seen:
                return [seen[target - nums[i]], i] # return indices, not nums!
            else:
                seen[nums[i]] = i
        return []