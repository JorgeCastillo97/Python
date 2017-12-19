from builtins import bool
from random import randint

board = []
attempts=4
for x in range(0,5):
    board.append(["O"]*5)

def printBoard(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0,len(board)-1)


def random_col(board):
    return  randint(0,len(board)-1)

print("Let's play Battleship!")
printBoard(board)
ship_row=random_row(board)
ship_column=random_col(board)

for t in range(attempts):
    guess_row = int(input("\nGuess Row: "))
    guess_col=int(input("\nGuess Col: "))

    if guess_row not in range(len(board)) or \
        guess_col not in range(len(board)):
        print("Out of range!")
    else:
        if ship_row == guess_row and ship_column == guess_col:
            print("You won!")
            break;
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed the battleship!")
            board[guess_row][guess_col]="X"
            printBoard(board)
    print(str(attempts-(t+1))+" attempt(s) left!")
    if t == (attempts-1):
        print("Game over.")