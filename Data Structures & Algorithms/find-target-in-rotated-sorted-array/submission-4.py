class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # neetcode solution
        # have conditions incorporating l, mid, r, and target

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]: return mid

            if nums[l] <= nums[mid]: # MID IS LEFT OF PIVOT
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else: # MID IS RIGHT OF PIVOT
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        # then solve my way
        # essentially implement find minimum/pivot
        # then call on the correct half