class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort nums # O(nlogn)
        # define return list
        nums.sort()
        solutions = []

        # LOOP - define/iterate a being first item, account for repeats as you move it to avoid dups
        for a, num_a in enumerate(nums):
            if a > 0 and num_a == nums[a-1]:
                continue
            # then do two sum II (pointer system) if sum too large/small move approp pointer, or append
            b, c = a+1, len(nums)-1
            while b < c:
                threeSum = nums[a] + nums[b] + nums[c]
                if threeSum < 0:
                    b += 1
                elif threeSum > 0:
                    c -= 1
                else:
                    solutions.append([num_a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b-1] and b<c:
                        b += 1
        # move pointers to avoid repeats
        # [0, 0, 0, 0]
        #  a
        #        b          
        #           c
        # valid answers are [[0,0,0]]
        # mine []
        return solutions


