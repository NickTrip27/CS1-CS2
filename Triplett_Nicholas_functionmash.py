'''

Authors: Nicholas Triplett
Date: 4/19/2024
Description: Has multiple functions that do a variety of things that interact with the user, and can be changed through the inputs. 
Bugs: None
Challenges: 1 - 2 - 3 - 4
Sources: https://www.w3schools.com/

'''

import random #Imports the random command library so the computer can read random commands 

def chorus (): #Starts a function under the function name chorus
    print("You are my sunshine")
    print("My only sunshine")
    print("You make me happy")
    print("When skies are gray")
    print("You'll never know, dear")
    print("How much I love you")
    print("Please don't take")
    print("My sunshine away")
def sing():#Starts a function under the function name sing 
    print("The other night, dear")
    print("As I lay sleeping")
    print("I dreamed I held you")
    print("In my arms")
    print("When I awoke, dear")
    print("I was mistaken")
    print("So I hung my head and cried")

def add(num1,num2):#Creates a function with two inputs under the name add
    print(num1 + num2)#Prints the sum of the two inputs 

def print_elements(my_list):#Creates a function with a list as the perameters under the name pring_elements
    for element in my_list:#Starts a for loop that scans each individual element in the input, my_list
        print(element)#Prints each individual element within the input, my_list 
def contains_element(my_list,element):#Creates a function with two perameters under the name contains_element 
    if element in my_list:#If the input element is in the list, my_list
        return True#The computer will return to the user True
    else:#Else the element is not within the list, my_list
        return False#The computer will return to the user False 
def multiply(num1,num2,num3):#Creates a function that has three perameters under the name multiply 
    print(num1 * num2 * num3)#Prints the product of the three perameters 
def even_odd(number): #Creates a function with one perameters under the name even_odd
    if number % 2 == 0:#If the input is divided by two and equals a whole number with no remainder 
        print("Even")#Print even to the user 
    else:#Else the number has a remainder when divided by two 
        print("Odd")#Print odd to the user
def is_int(string):#Creates a function with one input under the name is_int
    if "-" in string: #If there is a dash in the number entered
        string = string[1:]#Remove the dash 
    if string.isnumeric():#If the input is an integer
        return True #Return a value true
    else:#Otherwise 
        return False#Return a value false
def get_random():#Creates a function under the name get_random
    while True:#Starts a while true loop 
        firstnum = input("What is your first number?")#Asks the user for a number
        secondnum = input("What is your second number?")#Asks the user for a number

        if is_int(firstnum) and is_int(secondnum): #Checks if the two strings entered is an integer 
            print(random.randint(int(firstnum), int(secondnum))) #Converts the strings to integers 
            break #Breaks the while true so the code can keep running
        else:#If the number is not an integer
            print("Please enter an integer!")#Tell the user to enter an integer!
def replace_str(string, old_char, new_char):#Creates a function with three perameters
    new_string = ""#Creates a new variable new_string which will return in quotes as a string
    for s in string: #Starts a for loop scanning each letter(s) in the string 
        if s == old_char:# If a letter is the perameter old character 
            new_string += new_char #Add in the new character to the new string
        else:#Else if a letter (s) is not the perameter old character
            new_string += s #Add in the old characters to the new string
    return new_string #Return the new_string to the user with the changed letters 
def reverse_string(string): #Creates a function with one perameter
    return string[::-1] #Returns the perameter backwards by making the indexs opposites and backwards, reversing the string
def initials(name):#Creates a new function with one perameter
    name = name.split(" ")#If there is a space in the perameter, it will split the perameter
    initials = "" #Makes initials return in quotes as a string
    for n in name:#For each letter in the perameter
        initials += n[0]#Make the string initials the first letter of the peramter, index 0
    return initials #returns initials to the user

def palindrome(string): #Creates a function with one perameter
    return string == reverse_string(string)#Returns the string if the perameter is equal to the perameter revered. It uses the fast function for this.
def main():#Creates the main function that will hold all the fucntions, and run them 
    name = input("Enter you full name ")#Makes name equal to the input of the user
    print(initials(name))#Prints and runs the inintials function 
    print(palindrome(input("Ender a string and I will see if it is a palindrome")))#Prints and runs the palindrome function, setting the peramter equal to the users input 
    
    string = reverse_string(input("Enter a string and I will say it backwards!"))#Runs the reverse_string function with the string perameter equal to the users input
    print(string)#Prints the reverse string function
    chorus()#Runs the chorus funtion
    sing()#Runs the sing function
    chorus()#Runs the chorus function 
    add(1,3)#Runs the add function with the perameters 1,2
    my_list = ["Zach Bryan", "Tyler Childers", "Morgan Wallen"]#Makes a list called my_list
    print_elements(my_list)#Runs the print_element funtion withe my_list as the perameter 
    print(contains_element(my_list, "Zach Bryan"))#Print and run the contains element function with My_list and Zach Bryan as the perameters 
    print(replace_str("hello world","l","a"))#Print and run the replace string function with the string being hello world, and the other two perameters being l and a
    action = input("What would you like to do? 1. Multiply three numbers, 2. Check if your number is even or odd, 3. Print a random number between two given numbers, 4. See if your number is an integer! ")#Ask the user what action they want the computer to run between 4 actions 

    if action == "1":#If the user chooses action 1
        num1 = int(input("Enter number 1:"))#Asks for a number and turns it into an integer and assigns it to num1
        num2 = int(input("Enter number 2:"))#Asks for a number and turns it into an integer and assigns it to num2
        num3 = int(input("Enter number 3:"))#Asks for a number and turns it into an integer and assigns it to num3
        multiply(num1,num2,num3)#Runs the multiply function between the three given numbers 

    elif action == "2":#If the user chooses action 2
        number = int(input("What is the number you would like to check?"))#Asks the user for a number 
        even_odd(number)#Runs the even_odd function with the given number and perameter
    elif action == "3":#If the user chooses action 3
        get_random()#Runs the get_random function
    elif action == "4":#If the user chooses action 4
        string = input("Enter your number: ")#Asks the user for a number 
        print(is_int(string))#Prints and runs the is_int function
    else:#Otherwise
        print("Invalid")#Tell the user invalid
 
    

main()#runs the main function

#def function_name(inputs):
    #action
    #output (print or return)
 
    

                

    







