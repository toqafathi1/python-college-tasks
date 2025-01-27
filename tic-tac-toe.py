
# import random


# board = ["-", "-", "-",
#         "-", "-", "-",
#         "-", "-", "-"]
# currentPlayer = "X"
# winner = None
# gameRunning = True

# # game board
# def printBoard(board):
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print("---------")
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print("---------")
#     print(board[6] + " | " + board[7] + " | " + board[8])


# # take player input
# def playerInput(board):
#     inp = int(input("Select a spot 1-9: "))
#     if board[inp-1] == "-":
#         board[inp-1] = currentPlayer
#     else:
#         print("Oops player is already at that spot.")


# # check for win or tie
# def checkHorizontle(board):
#     global winner
#     if board[0] == board[1] == board[2] and board[0] != "-":
#         winner = board[0]
#         return True
#     elif board[3] == board[4] == board[5] and board[3] != "-":
#         winner = board[3]
#         return True
#     elif board[6] == board[7] == board[8] and board[6] != "-":
#         winner = board[6]
#         return True

# def checkRow(board):
#     global winner
#     if board[0] == board[3] == board[6] and board[0] != "-":
#         winner = board[0]
#         return True
#     elif board[1] == board[4] == board[7] and board[1] != "-":
#         winner = board[1]
#         return True
#     elif board[2] == board[5] == board[8] and board[2] != "-":
#         winner = board[3]
#         return True


# def checkDiag(board):
#     global winner
#     if board[0] == board[4] == board[8] and board[0] != "-":
#         winner = board[0]
#         return True
#     elif board[2] == board[4] == board[6] and board[4] != "-":
#         winner = board[2]
#         return True


# def checkIfWin(board):
#     global gameRunning
#     if checkHorizontle(board):
#         printBoard(board)
#         print(f"The winner is {winner}!")
#         gameRunning = False

#     elif checkRow(board):
#         printBoard(board)
#         print(f"The winner is {winner}!")
#         gameRunning = False

#     elif checkDiag(board):
#         printBoard(board)
#         print(f"The winner is {winner}!")
#         gameRunning = False


# def checkIfTie(board):
#     global gameRunning
#     if "-" not in board:
#         printBoard(board)
#         print("It is a tie!")
#         gameRunning = False


# # switch player
# def switchPlayer():
#     global currentPlayer
#     if currentPlayer == "X":
#         currentPlayer = "O"
#     else:
#         currentPlayer = "X"


# def computer(board):
#     while currentPlayer == "O":
#         position = random.randint(0, 8)
#         if board[position] == "-":
#             board[position] = "O"
#             switchPlayer()


# while gameRunning:
#     printBoard(board)
#     playerInput(board)
#     checkIfWin(board)
#     checkIfTie(board)
#     switchPlayer()
#     computer(board)
#     checkIfWin(board)
#     checkIfTie(board)

def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    Args:
        board: 3x3 list representing the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """
    Function to check if a player has won the game.
    Args:
        board: 3x3 list representing the current state of the board.
    Returns:
        True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def is_board_full(board):
    """
    Function to check if the board is full.
    Args:
        board: 3x3 list representing the current state of the board.
    Returns:
        True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    """
    Function to play the Tic-Tac-Toe game.
    """
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] != " ":
            print("Invalid move. Please try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


def main():
    """
    Main function to start the Tic-Tac-Toe game.
    """
    print("Welcome to Tic-Tac-Toe!")
    play_game()
    print("Thanks for playing.")


if __name__ == "__main__":
    main()
