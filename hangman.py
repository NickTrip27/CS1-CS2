import random #brings in random library for use of random functions
#creates a list, hangman_pics, of the visual progression of incorrect guesses in the game
hangman_pics = ['''              
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = ["hello","world","pyton"]           #creates the list of words that will the user will have to guess
secret = random.choice(words)               #selects a random word out of the list for the user 
secret_list = list(secret)                  #convert the secret word into a list by splicing the characters
hidden = []                                 #create an empty list to be used as a way for players to keep track of their guesses
guesses = 0                                 #variable to keep track of how many incorrect guesses the player has made; starts at zero
#adds to the hidden list such that the characters in the secret list line up with dashes to indicate the length etc of the word to the player
for character in secret_list:               #iterate through every eement (character) in the list of secret word's characters
    if character == " ":                    #if the character is a space 
        hidden.append("_ ")                 #add two spaces to the hidden list to demonstrate that there are multiple words 
    else:                                   #otherwise
        hidden.append("_ ")                 #add a dash and space to the hidden list to represent a character 


print ("".join(hidden))                     #converts the hidden list to a string, which is displayed, by joining each character in its list

while "_ " in hidden and guesses < len(hangman_pics) - 1:       #while there are still missing letters (dashes) and the player still has guesses remaining
    while True:                                                 #Begins the while true statement that will continualy running 
        guess = str.lower(input("Enter a letter: "))            #Asks the user to input a letter and sets it as a variable "guess"

        if guess not in list("abcdefghijklmnopqrstuvwxyz "):    #If the guess is not a letter
            print("Please enter a letter!")                     #Tell the user that their input was not a letter 
        else:                                                   #If the input is a letter
            break                                               #break the while true 

    if guess in secret_list:                                    #If the users letter guess is in the secret word 
        for index in range(len(secret_list)):                   #For every possible index (letter)
            if guess == secret_list[index]:                     #If the guess is in the index 
                hidden[index] = guess                           #
        
        print ("".join(hidden))                                 #
                
    else:
        print("Not here!")
        guesses += 1
        print(hangman_pics[guesses])
        

if "_ " in hidden:
    print(f"You lost! The word was (secret)")
else:
    print("You won!")
