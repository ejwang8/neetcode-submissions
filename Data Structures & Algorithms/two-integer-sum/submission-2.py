class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[1 3 5]; target = 6; i=0, j=2
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    return [i, j]