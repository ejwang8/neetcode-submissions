class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # essentially binary search on rows, then on column

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        mid_row = None

        # binary search on all rows
        while top <= bot:
            mid_row = (top + bot) // 2
            if target < matrix[mid_row][0]: # target smaller than first elem in row, move up
                bot = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else: break # if found it

        if top > bot: return False

        # binary search on that row
        l, r = 0, COLS - 1
        while l <= r:
            i = (l + r) // 2
            if matrix[mid_row][i] == target:
                return True
            elif target < matrix[mid_row][i]:
                r = i - 1
            else:
                l = i + 1

        return False
        