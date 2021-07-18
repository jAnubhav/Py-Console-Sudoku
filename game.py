from random import sample
from typing import List

def showBoard(board) -> None:
    for i in board:
        if board.index(i) % 3 == 0:
            print()
        for ind, j in enumerate(i):
            if ind % 3 == 0:
                print(' |', end="")
            print(j, '|', sep="", end="")
        print()

def createGame() -> List:
    row = [i * 3 + j for i in sample(range(3), 3) for j in sample(range(3), 3)]
    col = [i * 3 + j for i in sample(range(3), 3) for j in sample(range(3), 3)]
    num = sample(range(1, 10), 9)

    board = [[num[(3 * (r % 3) + r // 3 + c) % 9] for c in col] for r in row]
    sol, pos = [[] for i in range(9)], sample(range(81), 51)

    for i in range(81):
        sol[i // 9].append(board[i // 9][i % 9])
        if i in pos:
            board[i // 9][i % 9] = '_'
        
    return board, sol

if  __name__ == "__main__":
    print("\t Welcome")
    board, sol = createGame()
    showBoard(board)
    while True:
        while True:
            r = int(input("\nEnter the row : "))
            if r - 1 in range(9):
                break
            else:
                print("\nEnter a correct value")

        while True:
            c = int(input("\nEnter the column : "))
            if c - 1 in range(9):
                break
            else:
                print("\nEnter a correct value")

        while True:
            num = int(input("\nEnter the number : "))
            if num - 1 in range(9):
                break
            else:
                print("\nEnter a correct value")

        if board[r-1][c-1] == '_':
            board[r-1][c-1] = num
        else:
            print("\nEnter a correct row or a column")
        showBoard(board)
        
        if board == sol:
            print("Game Finished")
            break
