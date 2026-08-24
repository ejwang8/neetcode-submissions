class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # remember return l+1, r+2 bc 1-indexed
        while numbers[l] + numbers[r] != target and l < len(numbers)-1 and r > -1:
            if numbers[l] + numbers[r] < target: # too little
                l += 1
            else: # too big
                r -= 1
        return [l+1, r+1]


    # [1, 6, 8]
    # ==> targets could be 7, 9, or 14
    # if target 7, then 1 and 8. too big so move right to left then get 1 and 6
    # if target 9, start off 1 and 8 win
    # if target 14, 1 and 8 too big, so move left to right until 