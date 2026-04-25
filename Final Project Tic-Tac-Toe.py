PLAYER_X = "✖️"
PLAYER_O = "⭕"

#I chose emojis rather than "X" and "O" to make the game more readable

def create_board(): #Numbers to let player know the place of their selection
    return [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]


def print_board(board):
    print()
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("---+---+---")
    print()


def is_valid_move(board, position): #Checks if the move is valid or not
    if position < 1 or position > 9:
        return False

    row = (position - 1) // 3
    col = (position - 1) % 3

    if board[row][col] == PLAYER_X or board[row][col] == PLAYER_O:
        return False

    return True


def make_move(board, position, player): 
    row = (position - 1) // 3
    col = (position - 1) % 3
    board[row][col] = player


def check_winner(board, player): #Checks the winner based on placement 
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_draw(board): #Checks if it is a draw
    for row in board:
        for cell in row:
            if cell != PLAYER_X and cell != PLAYER_O:
                return False
    return True


def switch_player(current_player): #Lets the game goes between "X" and "O" each time
    if current_player == PLAYER_X:
        return PLAYER_O
    return PLAYER_X


def choose_mode(): #Extra game feature added, competitive is a best of three version of tic-tac-toe
    while True:
        print("Choose a game mode:")
        print("1. Normal Mode")
        print("2. Competitive Mode 🏆")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            return "normal"
        elif choice == "2":
            return "competitive"
        else:
            print("Invalid choice. Please enter 1 or 2.\n")


def play_round(): #Plays the game
    board = create_board()
    current_player = PLAYER_X

    while True:
        print_board(board)

        try:
            position = int(input(f"Player {current_player}  choose a position (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number only.\n")
            continue

        if not is_valid_move(board, position):
            print("Invalid move. Choose an available position from 1 to 9.\n")
            continue

        make_move(board, position, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player}  wins this round!")
            return current_player

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            return "Draw"

        current_player = switch_player(current_player)


def play_normal_mode(): #Normal mode
    print("\n🎮 Normal Mode Started!")
    play_round()


def print_scoreboard(score_x, score_o): #Keeps tracking of score
    print("\n🏆 Scoreboard")
    print(f"Player {PLAYER_X}  --> {score_x}")
    print(f"Player {PLAYER_O}  --> {score_o}\n")


def play_competitive_mode(): #Plays competitive
    print("\n🏆 Competitive Mode Started!")
    print("First player to win 2 rounds wins the match.\n")

    score_x = 0
    score_o = 0
    round_number = 1

    while score_x < 2 and score_o < 2:
        print(f"===== Round {round_number} =====")

        result = play_round()

        if result == PLAYER_X:
            score_x += 1
        elif result == PLAYER_O:
            score_o += 1

        print_scoreboard(score_x, score_o)
        round_number += 1

    if score_x == 2:
        print(f"🏆 Player {PLAYER_X}  wins the best of 3 match!")
    else:
        print(f"🏆 Player {PLAYER_O} wins the best of 3 match!")


def play_game(): #Final game play function
    print(f"🎮 Welcome to Tic-Tac-Toe!{PLAYER_X}  vs {PLAYER_O}\n")

    mode = choose_mode()

    if mode == "normal":
        play_normal_mode()
    else:
        play_competitive_mode()

play_game()

