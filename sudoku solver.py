# This function checks if a number can be placed in a specific position on the board
def validation(board:list[list[int]], row:int, col:int, num:int) -> bool:
    # Checks if the number is in the same row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Checks if the number is in the same column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Creates the values that will always return the top left (the start) of the 3x3 square grid
    corner_row = row - row % 3
    corner_col = col - col % 3
    
    # Checks if the number is in the same 3x3 square grid
    for i in range (3):
        for x in range(3):
            if board[corner_row + i][corner_col + x] == num:
                return False
        
    return True

def solve(board:list[list[int]],row:int,col:int):
    
    if col > 8:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if board[row][col] != 0:
        return solve(board, row, col+1)
    
    for num in range(1, 10):
        if validation(board, row, col, num):
            board[row][col] = num

            if solve(board, row, col+1):
                return True
            
        board[row][col] = 0
    
    return False


board = [ 
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

if solve(board, 0 ,0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()
else:
    print("There is no solution for this Sudoku")