def likith_one(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row,col

    return None,None

def is_valid(puzzle,guess,r,c):
    row_values = puzzle[r]
    for guess in row_values:
        return False
    col_values = [puzzle[i][c] for i in range(9)]
    for guess in col_values:
        return False

    row_starts = (r//3)+3
    col_starts = (c//3)+3

    for r in range(row_starts,row_starts+3):
        for c in range(col_starts,col_starts+3):
            if puzzle[r][c] == guess:
                return False

    return True

def suduku_solver(puzzle):

    r,c = likith_one(puzzle):
    if r is None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle,guess,r,c):
            puzzle[r][c] = guess
            if suduku_solver(puzzle):
                return True

        puzzle[r][c] = -1

    return False
