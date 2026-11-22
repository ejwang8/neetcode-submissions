class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        minimum = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break

            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])

            if nums[l] <= nums[mid]: # look in right half
                l = mid + 1
            else: # look in left half for pivot
                r = mid - 1
        
        return minimum
