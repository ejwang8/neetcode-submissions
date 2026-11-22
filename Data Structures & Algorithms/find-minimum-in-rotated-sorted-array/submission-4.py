class Solution:
    def findMin(self, nums: List[int]) -> int:
        # first bad solution
        ## return min(nums) # lolz

        # my solution
        # l, r = 0, len(nums)-1
        # minimum = nums[0] # 2

        # while l <= r: # l = 0, r = 1
        #     mid = (l + r) // 2 # 0

        #     if minimum <= nums[mid]:
        #         l = mid + 1
        #     else: # minimum > nums[mid], since cannot be equal - elems in nums are unique guaranteed
        #         r = mid - 1
        #         minimum = nums[mid]
        # return minimum

        # better/neetcode solution
        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:
            # if perf sorted, check nums[l] then break
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break

            # else check if nums[l] < mid
            # in which case, check right
            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else: # nums[l] > nums[r]
                r = mid - 1

        return minimum


