class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # neetcode solution
        # have conditions incorporating l, mid, r, and target

        # l, r = 0, len(nums)-1

        # while l <= r:
        #     mid = (l + r) // 2

        #     if target == nums[mid]: return mid

        #     if nums[l] <= nums[mid]: # MID IS LEFT OF PIVOT
        #         if nums[l] <= target <= nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1

        #     else: # MID IS RIGHT OF PIVOT
        #         if nums[mid] <= target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return -1

        # then solve my way
        # essentially implement find minimum/pivot
        # then call on the correct half

        l, r = 0, len(nums) - 1
        min_i = 0
        minimum = nums[min_i]
        
        while l <= r:
            if nums[l] < nums[r]:
                # minimum = min(minimum, nums[l])
                if nums[l] < minimum:
                    min_i = l
                    minimum = nums[l]
                break

            mid = (l + r) // 2
            # minimum = min(minimum, nums[mid])
            if nums[mid] < minimum:
                min_i = mid
                minimum = nums[mid]

            if nums[l] <= nums[mid]: # look in right half
                l = mid + 1
            else: # look in left half for pivot
                r = mid - 1

        l, r = 0, len(nums)-1
        if target == minimum: return min_i
        if nums[l] > nums[r]:
            if target >= nums[l]:
                r = min_i - 1
            else: 
                l = min_i + 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid]==target: return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1
