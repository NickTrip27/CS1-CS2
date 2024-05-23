'''
Author: Nicholas Triplett
Date: 11/20/2023
Description: Game where your can play the childhood game, Rock Paper Scissors against the computer. 
Bugs: None
Challenges: While True -- time -- str lower -- Score tracker
Sources: Mrs. Marciano 
'''
import random # imports random commands for the computer 
import time # imports time commands for pauses 

t = 1  # t is set to 1 second 


game = ["rock", "paper", "scissors"]  # makes the RPS list 


print("Welcome to Rock, Paper, Scissors! The rules are simple, choose a weapon, either rock, paper, or scissors, and see if you win!") #Prints the welcome into the game

while True: #starts the while true loop 
    time.sleep(2)  #puts a two second pause before asking if the user wants to play 
    play = str.lower(input("Would you like to play? It is first to 100 Points!"))#asks if the user wants to play while printing a question
    
    if play == "no": #if the user says no 
        print("Thank you for playing!") #it will print a thank you note, and will ask the user if they want to play again 
    elif play == "yes":  #if the user says yes, the progam will move to the next while true
        user_score = 0 # and set the user score to 0
        bot_score = 0 # and set the bot score to 0 

        while True: #starts a new while true loop 
            if user_score >= 100: #if users score ever reaches 100 or over
                print("You win!") #it will congragulate the user
                break # And move the program to the first while true loop
            elif bot_score >= 100: # if the computers score ever reaches 100 or over 
                print("You Loose!") # it will say the player lost,
                break #and move the program to the first while true loop


            user_weapon = str.lower(input("Choose a weapon, Rock, Paper, or Scissors! Or say 'stop' to stop playing!")) #Tells the player what they can choose, and if they want to stop playing the game
            bot_weapon = random.choice(game) #randomly chooses a weapon for the bot from the 'game' list
            if user_weapon == "stop":# if the user says stop
                print("Thanks for playing!") #it will thank the user for playing
                break # the program will move to the last while true loop 

            if user_weapon not in game: #if the users response is not one of the set responses 
                print("Invalid") #it will print invalid and restate the question 
            else: #Anything else the program will run this 
                print("I picked " + bot_weapon) #The computer will tell the user what it picked 
                                    
                if user_weapon == bot_weapon: # If both the weapons are the same 
                    print("Tie! No Points!") # The computer will say it is a tie, and give no points 

                elif user_weapon == "rock" and bot_weapon == "scissors": # If the user picks rock, and the bot chooses scissors
                    print("Winner!") # The computer will tell the user they won the round 
                    user_score +=25 # The computer will add 25 points to the users score
                    print(f"Your score is {user_score}") #The computer will print the users score 
                    print(f"My score is {bot_score}")# The computer will print the bots score 
                    
                elif user_weapon == "rock" and bot_weapon == "paper": #If the users weapon is rock, and the bots weapon is paper
                    print("Loser!") # The computer will tell the user they lost the round 
                    bot_score +=25 #The computer will add 25 points to the computers score 
                    print(f"Your score is {user_score}") #The computer will print the users score 
                    print(f"My score is {bot_score}") #The computer will print the computers score 
                     
                elif user_weapon == "scissors" and bot_weapon == "paper": #If the user pickes scissors, and the bot picks paper 
                    print("Winner!") # The computer will tell the user they won the round  
                    user_score +=25 # The computer will add 25 points to the users score 
                    print(f"Your score is {user_score}") # The computer will print the users score
                    print(f"My score is {bot_score}") # The computer will print computers 

                elif user_weapon == "scissors" and bot_weapon == "rock": # If the user picks scissors, and the bot picks rock 
                    print("Loser!") # The computer will print the user lost 
                    bot_score +=25 # The computer will add 25 points to its score 
                    print(f"Your score is {user_score}") # The computer will print the users score 
                    print(f"My score is {bot_score}") # The computer will print the computers score 
                   
                elif user_weapon == "paper" and bot_weapon == "scissors": #If the user picks paper, and the bot picks scissors  
                    print("Loser!") # the computer will tell the user they lost 
                    bot_score +=25 # the computer will add 25 points to the bots score 
                    print(f"Your score is {user_score}") # the computer will print the users score 
                    print(f"My score is {bot_score}") # the computer will print the computers score 
                    
                elif user_weapon == "paper" and bot_weapon == "rock": # If the user picks paper, and the bot picks rock 
                    print("Winner!") # The computer will tell the user they won 
                    user_score +=25 # The computer will add 25 points to the users score 
                    print(f"Your score is {user_score}") # The computer will print the users score 
                    print(f"My score is {bot_score}") # The computer will print the bots score 
