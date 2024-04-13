import random

# Constants
EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"
TIE = "TIE"
SIZE = 9

# Initialize game state
board = [EMPTY] * SIZE
current_player = PLAYER_X
game_running = True
winner = None

# Print the game board
def print_board():
    for i in range(0, SIZE, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

# Get player input
def player_input():
    while True:
        try:
            inp = int(input("Enter a position (1-9): ")) - 1
            if 0 <= inp < SIZE and board[inp] == EMPTY:
                board[inp] = current_player
                break
            else:
                print("Invalid input or position already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Check for a winner
def check_winner():
    global winner
    win_conditions = [
        # Horizontal lines
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # Vertical lines
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # Diagonal lines
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            winner = board[a]
            return True
    return False

# Check for a tie
def check_tie():
    global game_running
    if EMPTY not in board:
        print_board()
        print("It's a tie!")
        game_running = False

# Switch the current player
def switch_player():
    global current_player
    current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

# Computer move
def computer_move():
    while current_player == PLAYER_O and game_running:
        position = random.randint(0, SIZE - 1)
        if board[position] == EMPTY:
            board[position] = PLAYER_O
            switch_player()
            break

# Main game loop
while game_running:
    print_board()
    player_input()
    if check_winner():
        print_board()
        print(f"The winner is {winner}!")
        break
    check_tie()
    switch_player()
    computer_move()
    if check_winner():
        print_board()
        print(f"The winner is {winner}!")
        break
    check_tie()
