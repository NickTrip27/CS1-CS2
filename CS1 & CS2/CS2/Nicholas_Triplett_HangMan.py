'''
Name: Nicholas Triplett

Description: A hangman game that randomly chooses a word for you to guess

Bugs: You will loose a life if you enter a letter you already guessed

Features: None

Sources: W3 Schools - https://www.w3schools.com/ - Python for Everybody - Book - GeeksforGeeks - https://www.geeksforgeeks.org/ - Stack Overflow - https://stackoverflow.com/ - Google AI

Log: 1.0 (latest release)
'''
import random

fhand = open("words.txt", "r")                        #Opens the word txt which has all the words
words = fhand.readlines()                             #This reads each line and sets it like a list to the variable words
word = random.choice(words).strip()                   #This will randomly pick a word from words as the word for the game

step_1 = ("""                                         
  +---+
  |   |
      |
      |
      |
      |
========= """)                                        #Each one of these steps has a visual set to it depending on how many lives you have lost
step_2 = ('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
step_3 = ('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
step_4 = ('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
step_5 = ('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
step_6 = ('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
step_7 = ('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
print("Welcome to Hangman")
print(step_1)
        
def life_check(counter):  
  """
    This finds the display that needs to be printed depending on the amount of lives

    Args:
        counter: The amount of lives you have

    Returns:
        The visual that correlates to the amount of lives the user has left

    """        
  if counter == 6:                                      #If the user has 6 lives left, it will print step one, etc.
    print(step_1)
  elif counter == 5:
    print(step_2)
  elif counter == 4:
    print(step_3)
  elif counter == 3:
    print(step_4)
  elif counter == 2:
    print(step_5)
  elif counter == 1:
    print(step_6)


secret_word = ['_'] * len(word)                             #This creates the empty spaces that user sees and attempts to fill 
counter = 6                                                 #Creates a counter which is the users lives
while True:
  print(f"You have {counter} lives")                        #Shows the user how many lives he has 
  print(' '.join(secret_word))                              #This prints the empty spaces without quotes 
  choice = input("Guess a letter: ")                        #The letter the user guesses
  try:                                                      #This trys to see if the user input can be changed into an integer, and if it can, it asks the user to enter a letter, and if it can't, it continues with the code
    int(choice)                               
    print("Please enter a letter!")
  except ValueError:                                        
    if len(choice) == 1:                                    #This makes sure the user only entered one letter
      if choice in word:                                    #If the letter is in the word
        i = word.count(choice)                              #Counts how many times the letter is in the word 
        for i in range(len(word)):                          #For the amount of times the letter is used for every letter in the word 
            if word[i] == choice:                           #If the letter in the word matches
                secret_word[i] = choice                     #Then the letter will be displayed for the user by secret word 
        print("Correct!")
        print(' '.join(secret_word))                  
          
      elif choice not in word:                              #If the letter is not in the word
        print("Nope! You lost a life!")
        counter = counter - 1                               #The user loses a life and 1 is subtracted from the counter
      if '_' not in secret_word:                            #If there isn't anymore empty spaces in the secret word 
        print("You win!")                                   #The user wins and the game ends 
        break
      elif counter == 0:                                    #If the counter reaches 0 then the user is out of lives which means they lost 
        print("You lost!")
        print(f"The word was {word}")
        break                                               #Displays to the user they lost and ends the game 
    else:
      print("Enter a single letter!")


  life_check(counter)                                       #Runs the display function to show the appropriate image to the user

'''
Design the word selection and its storage 
Create the begining loop for the game which prompts the user
Implement input
Add the hangman displays
Win/Lose condition
Test 
Document 

Algo 
Set lives
Create Word
Create Diagram 
function
Get Guess
Check for existence 
Put it in sport 
Tries left 
Can the person guess the word(not necessary) 
Check win 
Check word function
Play again

''' 
  
    

   
    
    