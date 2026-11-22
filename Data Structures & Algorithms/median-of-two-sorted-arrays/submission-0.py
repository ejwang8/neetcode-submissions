class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # set A as smaller arr, B as longer

        # initialize l, r in A

        # loop through, def i and j midpoints in each arr
            # check if condition met, otherwise binary search
                # note account for edge case if i or j < 0 or > len(A/B)
                    # if condition met, check if odd/even, then return

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        total = len(A) + len(B)
        half = (len(A) + len(B)) // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            # i = 0, j = -1

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i < len(A) - 1 else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j < len(B) - 1 else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # if odd, return min of the like two nums to right of median
                if total % 2:
                    return min(Aright, Bright)
                else: # if even, first find max of two nums to left of median.
                        # then find min of two nums to right of median.
                        # THEN return avg of those two nums
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright: # current slice of A is too big
                r = i - 1
            else: # current slice of B too big
                l = i + 1
