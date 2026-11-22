class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums) # lolz

        l, r = 0, len(nums)-1
        minimum = nums[0] # 2

        while l <= r: # l = 0, r = 1
            mid = (l + r) // 2 # 0

            if minimum <= nums[mid]:
                l = mid + 1
            else: # minimum > nums[mid], since cannot be equal - elems in nums are unique guaranteed
                r = mid - 1
                minimum = nums[mid]
        return minimum
