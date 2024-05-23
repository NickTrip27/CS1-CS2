'''
Author: Nicholas Triplett
Date: 11/14/2023
Desription: Works like a magic eight ball, replying to yes or no questions with random responses.
Callenges: while true loop and if, elif, else statements
Bugs: None
Sources: https://www.pythonforbeginners.com/code-snippets-source-code/magic-8-ball-written-in-python
'''

import random #Imports the random module 

print("Hello world! I am the world famous eight-ball!") #Tells the user what the program is

while True:#starts a loop 
    knew = str.lower(input("Ask me anything! If you have nothing, say 'Stop' "))#asks the user to ask a question 
    
    if knew == "stop": #if the users respose is stop, the program stops the loop 
        break
    elif "?" in knew: # if the users respose has a question mark, it will insert a random response
        print(random.choice(["It is certain", "Reply hazy", "try again", "Don't count on it", "It is decidedly so", "Ask again later", "My reply is no", "Without a doubt", "Better not tell you now", "My sources say no", "Yes definitely", "Cannot predict now", "Outlook not so good"]))
    else: # If the program is anything else, it was tell the user it is not a question, and continue the loop 
        print("not a question!")

    
