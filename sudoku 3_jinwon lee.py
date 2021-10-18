board = [
    [0, 0, 2, 9, 5, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 3, 0, 0],
    [0, 9, 5, 0, 0, 0, 0, 0, 0],
    [1, 0, 7, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 1, 0, 0, 0, 0, 0, 5, 0]
]   

def find_empty(row, column, number):
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == number:
                return False

def print_board(board):                          
    for i in range(len(board)):                    
        if i % 3 == 0 and i != 0:               # i % 3 means when i is divisible by 3
            print("- - - - - - - - - - - -")    #this is for horizontal row at every 3 digit, to separate numbers on board into 9x9 sudoku format.
            
        for j in range (len(board[0])):
            if j % 3 == 0:                      #to ensure line not immediately printed on the left side.
                print(" | ", end="")            #for vertical column at every 3 digit, "" prevents infinite printing beyond 9x9 board
                
            if j == 8:                          
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") #make it stay on the same line


dddd