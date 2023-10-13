# REQUIREMENTS
#     We need to print a board.
#     Take in player input.
#     Place their input on the board.
#     Check if the game is won,tied, lost, or ongoing.
#     Repeat c and d until the game has been won or tied.
#     Ask if players want to play again.


def initialize_board():
    pass


def print_board(board):
    pass


def prompt_for_move():
    pass


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
