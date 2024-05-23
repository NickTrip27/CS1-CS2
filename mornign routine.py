'''
Authors: Nicholas Triplett
Date: 11/1/2023
Description: Interactive walkthrough of my morning routine,
which allows users to select their own options and gives different results depending on their routine 
Bugs: None
Challenges: While True - time import - str.lower
Sources:
https://www.digitalocean.com/community/tutorials/python-time-sleep
'''

print ("Alarm!") #Tell reader Alarm

import time  #brings in the time library for use of time functions 
t = 2 # sets time variable as 2 seconds
time.sleep(t) #wait designated time before continuing

while True: #Begins a while true loop that will continue until a break 
    snooze = str.lower(input("Snooze?")) #Asks if the user wants to snooze and store their response, in lowercase, in a variable snooze

    if snooze == "yes": #if the user responds with yes
        print("You have 5 more minutes of sleep") #Prints a statement for the reader 
        time.sleep(5)  #wait designated time before continuing
        print("Get up!") # Tells the reader to wake up 
        Break # Ends the while true loop 
    elif snooze == "no": #or, if the user responds with no, the computer will react with ___
        print("Get up!") #Tells the reader to wake up 
        Break #ends the while true loop 
    else: #if the user responds with anything but no or yes, the computer will react with ___
        print("Invalid") #Tells the reader their response in invalid and restates the question 

while True: #Begins a while true loop that will continue until a break 
    shower = str.lower(input("Did you shower last night?")) #Asks if the user showered 

    if shower == "yes": #if the user responds with yes, the computer will react with ___
        print("Go eat breakfast") # Tells the reader to go eat breakfast 
        Break # Ends the while true loop 
    elif shower == "no": #Or, if the user responds with no, the computer will react with ___
        print("Go shower!") #Tells the user to take a shower 

        while True: #Begins a while true loop that will continue until a break  
            time.sleep(5)  #wait designated time before continuing 
            done = str.lower(input("are you done?")) #Asks if the user is done showering, if they had not showered
            if done == "yes": #if the user responds with yes, the computer will react with ___
                print("Go eat breakfast") #Tells the reader to eat breakfast 
                Break #Ends the while loop 
        
            elif done == "no": #Or, if the user responds with no, the computer will react with ___
                print("You have to shower!") # Tells the reader to take a shower 

            
        Break #Ends the while true loop 
        
    else: #if the user responds with yes, the computer will react with ___
        print("Invalid") # Tells the user their response in invalid 
while True: #Begins a while true loop that will continue until a break 
    
    rain = str.lower(input("Will it rain today?")) #Asks the user if it is raining today 

    if rain == "yes": #if the user responds with yes, the computer will react with ___
        print("Wear your jacket and pack extra clothes!") # Tells the user to wear some closes because its raining 

        while True: #Begins a while true loop that will continue until a break 

            bag = str(input("Did you pack your rain clothes?")) #if it is raining, the computer will ask if you packed your clothes

            if bag == "yes": #if the user responds with yes, the computer will react with ___
                print ("Go pack your school bag and go to school!") #Tels the user to pack their school bag and head to school 
                time.sleep(3)  #wait designated time before continuing
                print ("Have Fun") # Tells the reader to have fun today 
                Break # Breaks the while true loop 
    
            elif bag == "no": #Or, if the user responds with no, the computer will react with ___
                print ("Go pack your rain clothes!!") # Tells the reader to pack rain clothes 

            else: #If the user responds with anything else, the computer will react with ___
                print("Invalid") # Tells the user their input is invalid 
                Break # Breaks the while true loop 
        Break # breaks another while true loop 
    elif rain == "no": #if the user responds with no, the computer will react with ___
        print("Pack your school bag, and go to school!") # tells the user to pack and head to school 
        time.sleep(3)  #wait designated time before continuing
        print("Have Fun!") #Wishes the reader to have fun 
        Break # breaks the while true loop 
    else: #if the user responds with anything else, the computer will react with ___
        print("invalid") # Tells the user their input was invalid 




