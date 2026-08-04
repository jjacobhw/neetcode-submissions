class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dupe = defaultdict(set)
        row_dupe = defaultdict(set)
        square_dupe = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                #check if current element is already in row, col or square
                if ( board[i][j] in row_dupe[i]
                    or board[i][j] in col_dupe[j]
                    or board[i][j] in square_dupe[(i // 3, j // 3)]):
                    return False

                row_dupe[i].add(board[i][j])
                col_dupe[j].add(board[i][j])
                square_dupe[(i//3,j//3)].add(board[i][j])
        return True
