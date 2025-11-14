from typing import List

class ValidSudoku:
    def validate_sudoku(self, board: List[List[int]]) -> int:
        # Check row
        for i in range(9):
            setts = set()
            for j in range(9):
                item = board[i][j]
                if item in setts:
                    return False
                elif item != '.':
                    setts.add(item)

        # Check Column
        for j in range(9):
            setts = set()
            for j in range(9):
                item = board[j][i]
                if item in setts:
                    return False
                elif item != '.':
                    setts.add(item)

        # Check Box
        start = [[0,0],[0,3],[0,6],
                 [3,0],[3,3],[3,6],
                 [6,0],[6,3],[6,6]
                ]
        for i, j in start:
            setts = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in setts:
                        return False
                    elif item != '.':
                        setts.add(item)

        return True

if __name__ == '__main__':
    sudoku = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
    s = ValidSudoku()
    print(s.validate_sudoku(board=sudoku))