# REQUIREMENTS
#     We need to print a board.
#     Take in player input.
#     Place their input on the board.
#     Check if the game is won,tied, lost, or ongoing.
#     Repeat c and d until the game has been won or tied.
#     Ask if players want to play again.

# Board is 3x3 array of numbers which could be 0 (blank), +1 (X) or -1 (O)
def initialize_board():
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]


def print_board(board):
    def get_marker(square):
        if square == 0:
            return ' '
        elif square < 0:
            return 'X'
        else:
            return 'O'

    board_string = '''
     ||     ||
  {}  ||  {}  ||  {}
     ||     ||
===================
     ||     ||
  {}  ||  {}  ||  {}
     ||     ||
===================
     ||     ||
  {}  ||  {}  ||  {}
     ||     ||
    '''
    board_args = [get_marker(square) for row in board for square in row]
    print(board_string.format(*board_args))


def prompt_for_starting_marker():
    while True:
        entry = input('Player 1, would you like to be X or O? ')
        if entry.upper() == 'X':
            print("Player 2 will be O")
            return -1
        elif entry.upper() == 'O':
            print("Player 2 will be X")
            return 1
        else:
            print("Pick one or the other!")


def switch_marker(marker):
    return -marker


def prompt_for_move():
    while True:
        entry = input('Enter a number 1 (upper left) through 9 (lower right) ')
        if entry.isdigit():
            move_num = int(entry)
            if 1 <= move_num <= 9:
                return move_num
        print('Not a valid move')


def get_board_coordinates(square):
    square -= 1
    return (square // 3, square % 3)


def apply_move(board, move, marker):
    coordinates = get_board_coordinates(move)
    board[coordinates[0]][coordinates[1]] = marker
    return board


def check_game_status(board):
    lines = (
        # Horizontals
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        # Verticals
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        # Diagonals
        (1, 5, 9),
        (7, 5, 3)
    )

    def check_line(line):
        total = 0
        for square in line:
            coordinates = get_board_coordinates(square)
            total += board[coordinates[0]][coordinates[1]]
        if total == 3:
            return 1
        elif total == -3:
            return -1
        else:
            return 0

    for line in lines:
        winner = check_line(line)
        if winner != 0:
            print(f'{"X" if winner < 0 else "O"} wins!')
            return True
    return False


def prompt_for_another_game():
    while True:
        entry = input("Play again? Y/N ")
        if entry.upper() == 'Y':
            return True
        elif entry.upper() == 'N':
            return False
        else:
            print('Not a valid entry')


def clear_screen():
    print("\n" * 100)


def main_loop():
    playing = True
    while playing:
        game_over = False
        board = initialize_board()
        marker = prompt_for_starting_marker()
        while not game_over:
            print_board(board)
            move = prompt_for_move()
            clear_screen()
            board = apply_move(board, move, marker)
            marker = switch_marker(marker)
            game_over = check_game_status(board)
        playing = prompt_for_another_game()


main_loop()
