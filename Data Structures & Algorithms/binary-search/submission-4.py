class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 # l=1, r=2
        while l <= r:
            i = (l + r) // 2 # i=1
            if nums[i] == target: return i
            elif nums[i] < target: l = i + 1
            else: r = i - 1
        return -1

        
        