'''
Name: Nicholas Triplett

Description: A Tick Tac Toe game that is played between two real users (No computer)

Bugs: Shouldn't be any bugs 

Features: None

Sources: W3 Schools - https://www.w3schools.com/ - Python for Everybody - Book - GeeksforGeeks - https://www.geeksforgeeks.org/ - Stack Overflow - https://stackoverflow.com/ - Google AI

Log: 1.0 (latest release)
'''

import random                                                   #Imports the random function 
print ("Welcome to Tick Tac Toe!")                              #Welcomes the user
possiblity = ["X", "O"]                                         #Creates a list of the two possible characters
board = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]                                                               #Creates the board and labels a number for every position on the board
def print_board(board):
    """
    Creates the board that is displayed to the user

    Args:
        board: the board filled with numbers 

    Returns:
        A 2D list which is the board that the players play on 

    """
    for row in range(len(board)):                               #For every row in the board, and each index and number in each row - this creates a number and coordinate X
        for column in range(len(board[row])):                   #For every column in the board, and each index and number in the individual column - this creates a number and coordinate for Y
            print(board[row][column], end= ' ')                 #print the coordinated index and form the board with spaces 
        print()
def pick_player_1(possibility):
    """
    Assignes a random character to play 1 

    Args:
        possibility: This is the list which has X or O which are the two available characters

    Returns:
        Character_1: The assigned character for player 1

    """
    character_1 = random.choice(possibility)                    #Randomly picks from the list
    return character_1
def pick_player_2(character_1):
    """
    Assignes player 2 their character based off of what player 1 is

    Args:
        character_1: This is the character which was previously randomly picked

    Returns:
        Character_2: This is player 2's character

    """
    if character_1 == "X":
        character_2 = "O"
        return character_2
    elif character_1 == "O":
        character_2 = "X"
        return character_2
def board_spot(spot, character_letter):
    """
    This changes the spot on the board to the players character. It uses the numbers on the board and their individual coordinates to be replaced by a character

    Args:
        spot: This is the number that the player inputted and the spot where they want to place 
        character_letter: This is respected character of the player

    Returns:
        This just changes the board and places a character over a number

    """
    
    if spot == 1:                                               
        board[0][0] = character_letter
    elif spot == 2:
        board[0][1] = character_letter
    elif spot == 3:
        board[0][2] = character_letter
    elif spot == 4:
        board[1][0] = character_letter
    elif spot == 5:
        board[1][1] = character_letter
    elif spot == 6:
        board[1][2] = character_letter
    elif spot == 7:
        board[2][0] = character_letter
    elif spot == 8:
        board[2][1] = character_letter
    elif spot == 9:
        board[2][2] = character_letter
 
def win(board):
    """
    This finds if there are any wins on the board

    Args:
        board: the board which is being edited after each player moves

    Returns:
        a true or false which when true means someone has won

    """
    if board[0][0] == board[0][1] == board[0][2]:               #If all of these coordinates equal each other on the board
        return True                                             #You return true
    elif board[1][0] == board[1][1] == board[1][2]:
        return True 
    elif board[2][0] == board[2][1] == board[2][2]:
        return True 
    elif board[0][0] == board[1][0] == board[2][0]:
        return True 
    elif board[0][1] == board[1][1] == board[2][1]:
        return True 
    elif board[0][2] == board[1][2] == board[2][2]:
        return True 
    elif board[0][0] == board[1][1] == board[2][2]:
        return True 
    elif board[0][2] == board[1][1] == board[2][0]:
        return True 
counter = 0                                                     #This sets the counter to 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]                           #This is used to make sure there is no overlaping

while True:
    game_type = input("Would you like A: Pick you characters. B: Randomly assign each other a character. ")
    game_type = game_type.lower()                               #Ask the player what they would like and changes their inputs to lowercase 
    if game_type == "a":                                        
        while True:                                             #This while true prompts player 1 to pick and choose their character and assigns both players their characters
                                                                #It is a while true so that the user must enter one of the prompted responses
            character_1 = input("Player 1, what would you like to be, X or O? ")
            if character_1 == "X":                              
                character_2 = "O"
                print(f"Player 1, you are {character_1}")
                print(f"Player 2, you are {character_2}")
                break
            elif character_1 == "O":
                character_2 == "X"
                print(f"Player 1, you are {character_1}")
                print(f"Player 2, you are {character_2}")
                break
            else:
                print("Please enter X or O")   
        break 
    elif game_type == "b":
        character_1 = pick_player_1(possiblity)
        print(f"Player 1, you are {character_1}")
        character_2 = pick_player_2(character_1)
        print(f"Player 2, you are {character_2}")
        break
    else:
        print("Please enter A or B")
print_board(board)
while counter <= 8:                                             #This is a while true however it breaks when the counter becomes greater than 8   
    while True:
        spot_1 = input(f"Player 1, you are up. Please enter a number on the board to place your {character_1}: ")
        try:                                                    #If the try is true, the spot inputed is removed from the list 
            spot_1 = int(spot_1)
            if spot_1 in numbers:
                numbers.remove(spot_1)
                break
            else:                                               #If the input has been removed from the list of numbers, that means the player is trying to overlap on the board which is not allowed
                print("You cannot do that!")
        except ValueError:                                      #If the input is not a number
            print("Enter a valid number!")       
    board_spot(spot_1, character_1)
    print_board(board)
    winner = win(board)
    if winner:                                                  #If the win board function is true...
        print(f"Congradulations Player 1, you Win!")
        break
    counter += 1                                                #When each turn happens, 1 is added to the counter
    if counter == 9:                                            #When the counter reaches 9, the board is full and there is a tie 
        break
    while True:
                                                                #This while true repeats everything in the previous loop, the only difference is this is player 2's turn 
                                                        
        spot_2 = input(f"Player 2, you are up. Please enter a number on the board to place your {character_2}: ")
        try:
            spot_2 = int(spot_2)
            if spot_2 in numbers:
                numbers.remove(spot_2)
                break
            else:
                print("You cannot do that!")
        except ValueError:
            print("Enter a valid number!")  
    board_spot(spot_2, character_2)
    print_board(board)
    winner = win(board)
    if winner:
        print(f"Congradulations Player 2, you Win!")
        break
    counter += 1
        

    

'''
1. Create a board and welcome the players done 
2. Assign each character randomly or by their choice done 
3. Create a loop that asks each play for their turns done 
    - Make sure the loop terminates after 9 turns and label it a tie done 
4. Give every number on the board its respective coordinates done 
5. Ask the user where they would like to place their character and replace it done 
6. Reprint the board between each turn done 
7. Create the win condition done 
    - Find all horizontal, virtical, and diagnal wins done 
8. Make sure all players cannot place a character on an already occupied space done 
9. Make sure you cannot enter letters done 
10. document 
'''