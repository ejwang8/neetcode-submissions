class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make it in set
        # look thru each item in list
        # check in num - 1 exists
            # if num - 1 exists ignore
            # if num - 1 does not exist start of sequence! keep tracking while loop if num + 1 exists...
        # return highest count

        numSet = set(nums)
        longest = 0
        # check if works on []empty

        for i in range(len(nums)):
            if (nums[i] - 1) not in numSet:
                length = 1
                while (nums[i] + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest