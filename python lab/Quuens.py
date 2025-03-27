import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:         
            return False
    return True
def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    def place_queen(row):
        if row == n:
            solutions.append(board[:])
            return True      
        columns = list(range(n))
        random.shuffle(columns)      
        for col in columns:
            if is_safe(board, row, col):
                board[row] = col
                if place_queen(row + 1):
                    return True
                board[row] = -1
        return False  
    place_queen(0)
    return solutions
def display_board(solution):
    n = len(solution)
    for row in range(n):
        for col in range(n):
            if solution[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
n = 8
solutions = solve_n_queens(n)
if solutions:
    print("One solution:")
    display_board(solutions[0])
else:
    print("No solution found.")
