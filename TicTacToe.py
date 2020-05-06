def display_board(board):
    print('\n'*100)
    board = ["", "   |   | \n " +  '{}'.format(board[1]) + " | " +   '{}'.format(board[2])  + " | " +  '{}'.format(board[3]) + " \n   |   | \n-----------", "   |   | \n " +  '{}'.format(board[4]) + " | " +   '{}'.format(board[5])  + " | " +  '{}'.format(board[6]) + " \n   |   | \n-----------" , "   |   | \n " +  '{}'.format(board[7]) + " | " +   '{}'.format(board[8])  + " | " +  '{}'.format(board[9]) + " \n   |   | \n" ]
    print (board[1])
    print (board[2])
    print (board[3])

def player_input():
    marker = ""
    marker = input("Player 1, Do you want to be X or O? ").upper()
    while marker != "":
        if marker == "X":
            player1 = "X"
            player2 = "O"
            print("Player 1, you are the X. Player 2, you are the 0")
            return player1, player2
        elif marker == "O":
            player1 = "0"
            player2 = "X"
            print("Player 1, you are the 0. Player 2, you are the X")
            return player1, player2
        else:
            marker = input("Insert a valid option ").upper()

def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[1] == board[5] == board[9] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[4] == board[5] == board[6] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[7] == board[8] == board[9] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[3] == board[5] == board[7] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[3] == board[6] == board[9] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[1] == board[4] == board[7] == mark:
        print("Congratulations! You have won!")
        return True
    elif board[2] == board[5] == board[8] == mark:
        print("Congratulations! You have won!")
        return True
    else:
        return False

import random

def choose_first():
    random_player = random.randint(1,2)
    print ("Player {} will go first".format(random_player))
    print ("Get ready to start")
    return random_player

def space_check(board, position):
    if board[position] != " ":
        return False
    return True

def full_board_check(board):
    for item in board:
        if item == " ":
            return False
        else:
            continue
    print("That was a tie!")
    return True

def player_choice(board):
    position = int(input("Choose your next position "))
    while space_check(board, position) is False:
        print ("The position is occupied. Please choose another position ")
        position = int(input("Choose your next position "))
    return position


def replay():
    option = ""
    option = input("Do you want to play again? Yes or No? ")
    while option != "":
        if option == "Yes":
            return True
        elif option == "No":
            return False
        else:
            option = input("Insert a valid option. Do you want to play again? Yes or no? ")

        print("Thank you for playing Tic Tac Toe!")


print('Welcome to Tic Tac Toe!')

while True:
    # while True:
    # Set the game up here
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(board)
    (player1, player2) = player_input()
    random_player = choose_first()
    # while game_on:
    while True:

        if random_player == 1:
            # Player 1 Starts
            position = int(player_choice(board))
            board = place_marker(board, player1, position)
            display_board(board)
            if win_check(board, player1):
                break
            if full_board_check(board) is True:
                break
            # Player2's turn
            position = int(player_choice(board))
            board = place_marker(board, player2, position)
            display_board(board)
            if win_check(board, player2):
                break
            if full_board_check(board) is True:
                break
        else:
            # Player2 starts
            position = int(player_choice(board))
            board = place_marker(board, player2, position)
            display_board(board)
            if win_check(board, player2):
                break
            if full_board_check(board) is True:
                break
            # Player1's turn
            position = int(player_choice(board))
            board = place_marker(board, player1, position)
            display_board(board)
            if win_check(board, player1):
                break
            if full_board_check(board) is True:
                break

    if not replay():
        print("Thank you for playing Tic Tac Toe!")
        break
