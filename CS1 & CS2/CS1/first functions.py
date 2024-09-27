'''

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

def add(num1,num2):
    print(num1 + num2)

def print_elements(my_list):
    for element in my_list:
        print(element)
def contains_element(my_list,element):
    if element in my_list:
        return True
    else:
        return False
def multiply(num1,num2,num3):
    print(num1 * num2 * num3)
def even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
def is_int(string):
    if "-" in string:
        string = string[1:]
    if string.isnumeric():
        return True
    else:
        return False
def get_random():
    while True:
        firstnum = input("What is your first number?")
        secondnum = input("What is your second number?")

        if is_int(firstnum) and is_int(secondnum):
            print(random.randint(int(firstnum), int(secondnum)))
            break
        else:
            print("Please enter an integer!")
def replace_str(string, old_char, new_char):
    new_string = ""
    for s in string:
        if s == old_char:
            new_string += new_char
        else:
            new_string += s
    return new_string
def reverse_string(string):
    return string[::-1]
def initials(name):
    name = name.split(" ")
    initials = ""
    for n in name:
        initials += n[0]
    return initials

def palindrome(string):
    return string == reverse_string(string)    
def main():
    name = input("Enter you full name ")
    print(initials(name))
    print(palindrome(input("Ender a string and I will see if it is a palindrome")))
    
    string = reverse_string(input("Enter a string and I will say it backwards!"))
    print(string)
    chorus()
    sing()
    chorus()
    add(1,3)
    my_list = ["Zach Bryan", "Tyler Childers", "Morgan Wallen"]
    print_elements(my_list)
    print(contains_element(my_list, "Zach Bryan"))
    print(replace_str("hello world","l","a"))
    action = input("What would you like to do? 1. Multiply three numbers, 2. Check if your number is even or odd, 3. Print a random number between two given numbers. ")

    if action == "1":
        num1 = int(input("Enter number 1:"))
        num2 = int(input("Enter number 2:"))
        num3 = int(input("Enter number 3:"))
        multiply(num1,num2,num3)

    elif action == "2":
        number = int(input("What is the number you would like to check?"))
        even_odd(number)
    elif action == "3":
        get_random()
    elif action == "4":
        string = input("Enter your number: ")
        print(is_int(string))
    else:
        print("Invalid")
 
    

main()

#def function_name(inputs):
    #action
    #output (print or return)
 
    

                

    







