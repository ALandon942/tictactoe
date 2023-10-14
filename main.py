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


def prompt_for_move():
    while True:
        entry = input('Enter a number 1 (upper left) through 9 (lower right) ')
        if entry.isdigit():
            move_num = int(entry)
            if 1 <= move_num <= 9:
                return move_num
        print('Not a valid move')


def apply_move(move):
    pass


def check_game_status():
    pass


def prompt_for_another_game():
    pass


playing = True
while playing:
    game_over = False
    board = initialize_board()
    while not game_over:
        print_board(board)
        move = prompt_for_move()  # includes prompting for X or O
        board = apply_move(move)
        game_over = check_game_status()
    playing = prompt_for_another_game()