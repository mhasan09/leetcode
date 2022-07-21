from collections import defaultdict


def isValidSudoku(board):
    row_bag = defaultdict(set)
    col_bag = defaultdict(set)
    sec_bag = defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if not num.isdigit():
                continue

            sec = (i // 3, j // 3)
            if num in row_bag[i] or num in col_bag[j] or num in sec_bag[sec]:
                return False
            else:
                row_bag[i].add(num)
                col_bag[j].add(num)
                sec_bag[sec].add(num)
    return True


print(isValidSudoku(
    [[".", ".", "4", ".", ".", ".", "6", "3", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
     [".", ".", ".", "5", "6", ".", ".", ".", "."],
     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
     [".", ".", ".", "7", ".", ".", ".", ".", "."],
     [".", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
