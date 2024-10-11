import random
from IPython.display import clear_output

# Helper Functions

import os

def display_board(board):
    
    os.system('clear')
    
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    # Output: (Player 1 marker, Player 2 marker)
    player_choice = ''
    while player_choice != 'X' and player_choice != 'O':
        player_choice = input("Player 1: Enter your choice - X or O: ").upper()
    if player_choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def choose_first():
    first_player = random.randint(0, 1)
    if first_player == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def board_position(board, player_choice, position):
    board[position] = player_choice

def win_check(board, mark):
    # Check all win conditions: rows, columns, diagonals
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark))

def isSpace(board, position):
    # Checks if the board's position is empty
    return board[position] == '  '

def isFull(board):
    # Checks if the board is full
    return '  ' not in board[1:]  # Ignore index 0

def player_nextchoice(board):
    # Ensures the player chooses a valid and empty position
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not isSpace(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position

def replay():
    choice = input("Want to play again? Yes or No: ").strip().lower()
    return choice == 'yes'

# Main Game Logic

print("Welcome to the Tic-Tac-Toe Game")

while True:
    game_board = ['  '] * 10  # Initialize board with 10 spaces (index 0 is ignored)
    player_one, player_two = player_input()  # Get player markers

    turn = choose_first()  # Randomly choose the starting player
    print(turn + ' will go first')

    play_game = input('Ready to play? Enter y or n: ')

    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(game_board)
            position = player_nextchoice(game_board)
            board_position(game_board, player_one, position)

            if win_check(game_board, player_one):
                display_board(game_board)
                print("Player 1 has WON!!")
                game_on = False
            else:
                if isFull(game_board):
                    display_board(game_board)
                    print("This game is a tie!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(game_board)
            position = player_nextchoice(game_board)
            board_position(game_board, player_two, position)

            if win_check(game_board, player_two):
                display_board(game_board)
                print("Player 2 has WON!!")
                game_on = False
            else:
                if isFull(game_board):
                    display_board(game_board)
                    print("This game is a tie!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break