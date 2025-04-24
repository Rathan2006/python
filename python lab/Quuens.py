import numpy as np

n = int(input("Enter n: "))

s = [" "] * (n * n)
board = np.array(s)
board = board.reshape((n, n))
ans = []

def isSafe(board, row, col, n):
    #checking in column vertically up
    for i in range(row, -1, -1):
        if board[i][col] == 'Q':
            return False
    
    #right diagonal
    i, j = row, col
    while(i >= 0 and j < n):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    #left diagonal
    i, j = row, col
    while(i >= 0 and j >= 0):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True
    

def nQueens(board, row, n, ans):
    if (row == n):
        ans.append(board.copy())
        return
    
    for i in range(n):
        if (isSafe(board, row, i, n)):
            board[row][i] = 'Q'
            nQueens(board, row + 1, n, ans)
            board[row][i] = ' '

nQueens(board, 0, n, ans)

print("Favourable Positions: ")
for _ in ans:
    print(_)
    print(" - - " * n)