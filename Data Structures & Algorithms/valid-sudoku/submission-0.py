class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # double loop
        # o(3) to look up row, column, and cell

        from collections import defaultdict

        row_check = defaultdict(set)
        col_check = defaultdict(set)
        square_check = defaultdict(set)

        for y in range(len(board)):
            for x in range(len(board)):
                num = board[y][x]

                # check if in any of the three, if so return Faslse
                # if not add to the hash
                if num == '.': continue
                if num in col_check[x] or num in row_check[y] or num in square_check[(x // 3, y // 3)]:
                    return False
                else:
                    col_check[x].add(num)
                    row_check[y].add(num)
                    square_check[(x // 3, y // 3)].add(num)
        
        return True