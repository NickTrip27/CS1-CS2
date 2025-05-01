'''
Name: Nicholas Triplett

Description: A battle ship game where a user places against a ship

Bugs: Shouldn't be any

Features: None

Sources: W3 Schools - https://www.w3schools.com/ - Python for Everybody - Book - GeeksforGeeks - https://www.geeksforgeeks.org/ - Stack Overflow - https://stackoverflow.com/ - Google AI

Log: 1.0 (latest release)

Kaki and Luke Weiksner tested this code
'''
import random
a = '0'
b = '0'
c = '0'
d = '0'
e = '0'
f = '0'
g = '0'
h = '0'
i = '0'
j = '0'
k = '0'
l = '0'
m = '0'
n = '0'
o = '0'
p = '0'
q = '0'
r = '0'
s = '0'
t = '0'
u = '0'
v = '0'
w = '0'
x = '0'
y = '0'                                         #This sets the individual spaces on the board 0

print("Welcome to Battleship! To begin, enter the cordinate you would like to place your first ship and so on.")


def grid(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y):
    """
    Creates the board with all the letters which serve as variables for numbers or Hit or Miss icons

    Args:
        the letter: Each of these letters equals a certain visual. Either 0 or an H or an M

    Returns:
        A 2D array that is easy for the user to look at.

    """
    print(f'''
    \033[4m       0|1|2|3|4 \033[0m
        0| {a} {b} {c} {d} {e}
        1| {f} {g} {h} {i} {j} 
        2| {k} {l} {m} {n} {o}
        3| {p} {q} {r} {s} {t}
        4| {u} {v} {w} {x} {y} ''')              #The slashes underline the line
grid(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y)

board1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]                                                               #Creates the board and labels a number for every position on the board
board2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]    


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

def place_ship(board,x,spots,theirspots):
    """
    Creates the users board by asking the user where to place their ships 

    Args:
        board: The board which this function changes depending on the input
        x: The number of ship the user is inputing for. Ship 1. Ship 2. etc
        spots: The spots which the user has already placed
        theirspots: the coords the user places 

    Returns:
        A user board with all of their ships on it

    """
    coords = ['0', '1', '2', '3', '4']
    while True:
        ship = input(f"Ship {x}: ")
        lenser = len(ship)
        if lenser == 3 and ship[0] in coords and ship[2] in coords and ship[1] == ',' and ship not in theirspots:
            #This if statement checks to make sure the user's input is the way it should be.It checks if the lenght is proper, and if the numbers are proper
            theirspots.append(ship)
            combined_guess = str(ship[0]) + str(ship[2])        #This takes the numbers the user inputed and puts them together like 11 not 1+1
            spots.append(combined_guess)
            row = ship[0]
            row = int(row)
            column = ship[2]
            column = int(column)
            ships = '\033[1;31mS\033[0m'                        #This makes the ship red
            board[row][column] = ships
            break
        else:
            print("Please enter a proper coordinate")
def computership(board,places):
    """
    Creates the computers board with all of the ships on it

    Args:
        board: the board filled with numbers(it uses a different board then the user)
        places: the places which the computer has already places a ship

    Returns:
       the computer board with all of the places on it 

    """
    numbers = [0, 1, 2, 3, 4]
    x = 1
    while x != 6:
        while True:
            row = random.choice(numbers)
            column = random.choice(numbers)         #randomly pick an X and Y value
            ships = '\033[1;31mS\033[0m'
            board[row][column] = ships
            combined_string = str(row) + str(column)   
            if combined_string not in places:       #It combines the coords and makes sure its not repeated 
                break
        places.append(combined_string)

        x += 1
def computer_guess(board,spots,places,wincon):
    """
    Creates a guess for the computer

    Args:
        board: the players board filled with their numbers 
        spots: the users spots of where their ships are
        places: the places where the computer has guessed
        wincon: the computers win condition

    Returns:
        wincon: which either raises or stays the same depending on if it guesses a team

    """
    while True:
        hit = '\033[32mH\033[0m'
        miss = '\033[34mM\033[0m'                #This just colors the letters 
        numbers = [0, 1, 2, 3, 4]
        row = random.choice(numbers)
        column = random.choice(numbers)         #Randomly guess a y and x falue 
        combined_guess = str(row) + str(column)
        if combined_guess not in places:
            if combined_guess in spots:
                board[row][column] = hit
                places.append(combined_guess)
                wincon += 1                     #if the y and x value are one of the coords for the users ship, it makes a hit and adds 1 to wincon 
            else:
                board[row][column] = miss
                places.append(combined_guess)
            return wincon
        
        


    
spots = []
places = []
computership(board1, places)                    #This makes the computers board without printing it 

io = 1
while True:
    theirspots = []
    print("To place your ship, enter the coordinates you want your ship to be on! The first digit is your X axis and the second digit is you Y axis. Place a comma inbetween your digits. (For example: 1,2): ")
    while io != 6:
        place_ship(board2,io,spots,theirspots)  #This creates a loop for the users guess's for 5 ships 
        io += 1
    print_board(board2)
    break

letters = []
print("Above, is your board with your ships on it!↑↑↑↑↑↑↑↑ Only you can see your ships, the computer can't.")
print(f"This is your guessing board below. ↓↓↓↓↓")
grid(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y)
win = 0
places2 = []
theirspots1 = []
wincon = 0
while True:
    coords = ['0', '1', '2', '3', '4']
    guess = input("Enter a coordinate to guess a spot on the board. The first digit is your X axis and the second digit is you Y axis. Place a comma inbetween your digits. (For example: 1,2): ")
    lenser1 = len(guess)
    if lenser1 == 3 and guess[0] in coords and guess[2] in coords and guess[1] == ',' and guess not in theirspots1:
        theirspots1.append(guess)
        #This asks the user for their guess and it makes sure that the guess is a valid input and that it follows the following things. It also appends their guess to theirspots1 which records their previous spots so they can't guess it again 
        combined_guess = str(guess[0]) + str(guess[2])
        if combined_guess in places:
            #This huge if, elif finds if the users guess is one of the computers ship, it finds which coordinate they inputed and it switches the variable to a hit sign
            let = '\033[32mH\033[0m'
            win += 1
            if guess == '0,0':
                a = let
            elif guess == '1,0':
                b = let
            elif guess == '2,0':
                c = let
            elif guess == '3,0':
                d = let
            elif guess == '4,0':
                e = let
            elif guess == '0,1':
                f = let
            elif guess == '1,1':
                g = let
            elif guess == '2,1':
                h = let
            elif guess == '3,1':
                i = let
            elif guess == '4,1':
                j = let
            elif guess == '0,2':
                k = let
            elif guess == '1,2':
                l = let
            elif guess == '2,2':
                m = let
            elif guess == '3,2':
                n = let
            elif guess == '4,2':
                o = let
            elif guess == '0,3':
                p = let
            elif guess == '1,3':
                q = let
            elif guess == '2,3':
                r = let
            elif guess == '3,3':
                s = let
            elif guess == '4,3':
                t = let
            elif guess == '0,4':
                u = let
            elif guess == '1,4':
                v = let
            elif guess == '2,4':
                w = let
            elif guess == '3,4':
                x = let
            elif guess == '4,4':
                y = let
            wincon = computer_guess(board2,spots,places2,wincon)
            {print_board(board2)}                                   #This prints the users board which the computer is guess on so the user sees how their ships are holding up
            print("This is your board after the computers turn above.↑↑↑↑")
            print("Below is your guessing board below. ↓↓↓↓↓")
            print(f'''
        \033[4m       0|1|2|3|4 \033[0m
            0| {a} {b} {c} {d} {e}  |   
            1| {f} {g} {h} {i} {j}  |
            2| {k} {l} {m} {n} {o}  |
            3| {p} {q} {r} {s} {t}  |
            4| {u} {v} {w} {x} {y}  | ''')
            if win == 5:
                print("You won!")
                break
            elif wincon == 5:
                print("You lost, computer beat you!")
                break                                               #These to if, elif check if either the computers win condition or the users win conditon has hit the max, and if it does one of them won 
        elif combined_guess not in places:
            #This if, elif jumble is similar to the last, but if the users guess is not a computer ship, it finds the coordiante they guessed and it replaces the variable with a miss sign 
            let = '\033[34mM\033[0m'
            if guess == '0,0':
                a = let
            elif guess == '1,0':
                b = let
            elif guess == '2,0':
                c = let
            elif guess == '3,0':
                d = let
            elif guess == '4,0':
                e = let
            elif guess == '0,1':
                f = let
            elif guess == '1,1':
                g = let
            elif guess == '2,1':
                h = let
            elif guess == '3,1':
                i = let
            elif guess == '4,1':
                j = let
            elif guess == '0,2':
                k = let
            elif guess == '1,2':
                l = let
            elif guess == '2,2':
                m = let
            elif guess == '3,2':
                n = let
            elif guess == '4,2':
                o = let
            elif guess == '0,3':
                p = let
            elif guess == '1,3':
                q = let
            elif guess == '2,3':
                r = let
            elif guess == '3,3':
                s = let
            elif guess == '4,3':
                t = let
            elif guess == '0,4':
                u = let
            elif guess == '1,4':
                v = let
            elif guess == '2,4':
                w = let
            elif guess == '3,4':
                x = let
            elif guess == '4,4':
                y = let
            wincon = computer_guess(board2,spots,places2,wincon)


            {print_board(board2)}
            print("This is your board after the computers turn above. ↑↑↑↑↑")
            print("Below is your guessing board below. ↓↓↓↓↓")
            print(f'''
        \033[4m       0|1|2|3|4 \033[0m
            0| {a} {b} {c} {d} {e}  |   
            1| {f} {g} {h} {i} {j}  |
            2| {k} {l} {m} {n} {o}  |
            3| {p} {q} {r} {s} {t}  |
            4| {u} {v} {w} {x} {y}  | ''')
            if wincon == 5:
                print("You lost, computer beat you!")
                break

    else:
        print("Please enter a valid Coordinate!")
    
    




