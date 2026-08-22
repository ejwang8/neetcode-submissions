class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        # prefix pass
        for i in range(1, len(nums)): # 1, 2, 3
            output[i] = output[i-1]*nums[i-1]

        # postfix pass
        postfix = 1
        for i in range(len(nums)-2, -1, -1): # 2, 1, 0
            postfix *= nums[i+1]
            output[i] *= postfix

        return output
