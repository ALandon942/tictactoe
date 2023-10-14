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


def apply_move(board, move, marker):
    move -= 1
    board[move // 3][move % 3] = marker
    return board


def check_game_status():
    pass


def prompt_for_another_game():
    while True:
        entry = input("Play again? Y/N ")
        if entry.upper() == 'Y':
            return True
        elif entry.upper() == 'N':
            return False
        else:
            print('Not a valid entry')


def main_loop():
    playing = True
    while playing:
        game_over = False
        board = initialize_board()
        marker = prompt_for_starting_marker()
        while not game_over:
            print_board(board)
            move = prompt_for_move()
            board = apply_move(board, move, marker)
            marker = switch_marker(marker)
            game_over = check_game_status()
        playing = prompt_for_another_game()


main_loop()

