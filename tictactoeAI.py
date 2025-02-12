import random

# Global variables
board = ["-"] * 9
player = "X"
winner = None
game_active = True
ai_level = None  # AI difficulty level

# Function to display the board
def lboard(board):
    print("\n+---+---+---+")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i + 1], "|", board[i + 2], "|")
        print("+---+---+---+")

# Get AI difficulty level
def choose_ai_level():
    global ai_level
    while True:
        level = input("Choose AI level (1: Beginner, 2: Intermediate, 3: Pro): ")
        if level in ["1", "2", "3"]:
            ai_level = int(level)
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

# Player input or AI move
def l3ab():
    if player == "X":  # Human player
        while True:
            try:
                position = int(input("Choose a position (1-9): ")) - 1
                if 0 <= position <= 8 and board[position] == "-":
                    return position
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Enter a valid number.")
    else:  # AI move
        return ai_move()

# AI Decision Making
def ai_move():
    if ai_level == 1:
        return beginner_ai()
    elif ai_level == 2:
        return intermediate_ai()
    else:
        return pro_ai()

# **BEGINNER AI: Random Moves**
def beginner_ai():
    available_positions = [i for i in range(9) if board[i] == "-"]
    return random.choice(available_positions)

# **INTERMEDIATE AI: Blocks & Wins**
def intermediate_ai():
    # Check if AI can win
    for pos in range(9):
        if board[pos] == "-":
            board[pos] = "O"
            if check_winner_ai():
                return pos  # Make the winning move
            board[pos] = "-"  # Undo move

    # Check if AI needs to block player
    for pos in range(9):
        if board[pos] == "-":
            board[pos] = "X"
            if check_winner():
                board[pos] = "-"  # Undo move
                return pos  # Block the player
            board[pos] = "-"  # Undo move

    # Otherwise, play randomly
    return beginner_ai()

# **PRO AI: Minimax Algorithm**
def pro_ai():
    best_score = -float("inf")
    best_move = None

    for pos in range(9):
        if board[pos] == "-":
            board[pos] = "O"
            score = minimax(board, False)
            board[pos] = "-"  # Undo move
            if score > best_score:
                best_score = score
                best_move = pos

    return best_move

# Minimax Algorithm for Pro AI
def minimax(board, is_maximizing):
    if check_winner_ai():
        return 1 if winner == "O" else -1
    if "-" not in board:
        return 0  # Tie

    if is_maximizing:
        best_score = -float("inf")
        for pos in range(9):
            if board[pos] == "-":
                board[pos] = "O"
                score = minimax(board, False)
                board[pos] = "-"
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for pos in range(9):
            if board[pos] == "-":
                board[pos] = "X"
                score = minimax(board, True)
                board[pos] = "-"
                best_score = min(best_score, score)
        return best_score

def check_winner_ai():
    global winner
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            winner = board[condition[0]]
            # print(f"Player {winner} wins!")
            return True
    return False
"""def minimax(board, is_maximizing, depth=0):
    # Base cases: Check if the game is over
    result = evaluate_board()
    if result is not None:
        return result  # Return score if there's a winner or tie

    if is_maximizing:
        best_score = -float("inf")
        for pos in range(9):
            if board[pos] == "-":
                board[pos] = "O"
                score = minimax(board, False, depth + 1)
                board[pos] = "-"  # Undo move
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for pos in range(9):
            if board[pos] == "-":
                board[pos] = "X"
                score = minimax(board, True, depth + 1)
                board[pos] = "-"  # Undo move
                best_score = min(best_score, score)
        return best_score
"""
# Check for a winner
def check_winner():
    global winner
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            winner = board[condition[0]]
            print(f"Player {winner} wins!")
            return True
    return False

# Check for a tie
def check_tie():
    if "-" not in board:
        print("It's a tie!")
        return True
    return False

# Switch player
def switch_player():
    global player
    player = "X" if player == "O" else "O"

# **Main Game Loop**
choose_ai_level()
while game_active:
    lboard(board)
    move = l3ab()
    board[move] = player

    if check_winner() or check_tie():
        lboard(board)
        break

    switch_player()
