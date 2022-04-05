def make_board():
    board = [[0 for x in range(9)] for y in range(9)]
    board[0][2]=4
    board[0][3]=9
    board[0][4]=1
    board[0][6]=8
    board[0][7]=6
    board[0][8]=5
    
    board[1][4]=8
    board[1][5]=7
    board[1][7]=4
    board[1][8]=3
    
    return board

def print_board (board):
    for rownum in range(9):
        row = board[rownum]
        #print (row)
        for space in row:
            print (space,end='')
        print ()
        #if rownum == 2 or rownum == 5:
        if rownum % 3 == 2 and rownum < 8:
            print ('-----------------------------------')
            
def check_col (column, num, board):
    #return False if num appears in column
    for row in board:
        if row[column] == num:
            return False
    return True
    
def check_block (column, row, num, board):
    #check if num is in 1st sublock
    #returns false if num present
    basecol = (column//3)*3
    baserow = (row//3)*3 #baserow = row - (row % 3)
    for r in range(3):
        for c in range(3):
            if board[baserow+r][basecol+c] == num:
                return False
    return True
    
def next_spot (row, column):
    newrow = row
    newcolumn = column + 1
    if column == 8: #end or row
        newrow += 1
        newcolumn = 0
    return newrow, newcolumn
    
def solve_spot (board, row, column):
    #print (row, column)
    if row == 9: #only way to have row = 9 is if board is solved!
        return True
    if board[row][column] != 0: #spot is filled
        newrow, newcolumn = next_spot(row, column)
        return solve_spot(board, newrow, newcolumn)
    for num in range(1, 10):
        if check_col(column, num, board) and num not in board[row] \
        and check_block(column, row, num, board):
            board[row][column] = num
            newrow, newcolumn = next_spot(row, column)
            if solve_spot(board, newrow, newcolumn) == True:
                return True
            board[row][column] = 0
    return False
            
    
    
def solve_board(board):
    print ('Here we go!')
    x = solve_spot(board, 0, 0)
    if x == True:
        print ('We solved it!')
    else:
        print ('No solution')
    print_board(board)
    
b = make_board()
solve_board(b)

    