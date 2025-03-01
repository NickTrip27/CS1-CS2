'''
Name: Nicholas Triplett

Description: Is a menu of functions that are supposed to preform for an inputed name or word. The functions do not use functions of the string class

Bugs: None

Features: Menu - Boolean return for title/distiction

Sources: https://www.w3schools.com/python/python_for_loops.asp , Classroom resources such as Mr. Campbell and Ms. Marciano

Log: 1.0 (Latest release)
'''
import random
functions = ['Print your Firstname, Middlename(s), and Lastname', 'Reverse your name/word', 'Find the number of vowels in your name/word', 'Count a certain amount of letters in your name/word', 'Find the consonant frequency in your name/word', 'Convert your name/word into lowercase', 'Convert your name/word into uppercase', 'Shuffle the letters in your name/word', 'Find if there is a hyphen in your lastname or word', 'Find if your firstname or word is a palindrome', 'Print your initials', 'Find if your name has a title/distinction']
print("Hello and welcome to the WhatsinaName menu!")
def firstname(split_name):
    """
    Description: This finds the firstname of the entered name 

    Args:
        split_name - This is the enter name split by spaces

    Returns:
        The first index or the firstname 

    """
    firstname_1 = split_name[0]                                     #set firstname as the first index
    return firstname_1
def middlename(split_name):
    """
    Description: This finds the middle name or names of the inputed name by subtracting the first and last two indexes from the list

    Args:
        split_name - The inputed name split into a list by spaces

    Returns:
        Essentially returns the split_name without the first and last names. 

    """
    middlename = split_name[1: -1]                                  #set middle name as split_name without the first and last names
    return (' '.join(middlename))                                   #return the string without commas or quotes
def lastname(split_name):
    """
    Description: This finds the lastname

    Args:
        split_name - The inputed name split into a list by spaces

    Returns:
        The last index of split_name

    """
    lastname = split_name[-1]                                       #Set lastname as the last index of the list
    return lastname
def reverse(word):
    """
    Description: This reverses the name or inputed word

    Args:
        word - the inputed name or word 

    Returns:
        drow - the inputed word but backwards

    """
    drow = word[::-1]                                               #Set drow as the word backwards
    return drow
def vowels(word):
    """
    This finds the amount of vowels in the inputed word/name

    Args:
        word - the inputed name or word 

    Returns:
        vowelcounter - the number of vowels in word

    """
    vowelcounter = 0                                                #Setting the vowelcounter to zero 
    vowels = ("aeiouAEIOU")                                         #The vowels 
    for letter in word:                                             #checking each letter in the word
        if letter in vowels:
            vowelcounter += 1                                       #if the letter is a vowel, it adds 1 to the vowelcounter
    return vowelcounter
def counterletter(letter, word):
    """
    This finds the certain amount of letters that the user wants the program to find

    Args:
        word - the inputed name or word 
        letter - the inputed letter which the user wants to find the amount of 

    Returns:
        counter - the number of times the certain letter is in the word

    """
    counter = 0
    for i in word:                                                  #for each letter in the word
        if i is letter: 
            counter += 1                                            #if the letter is the letter which the user wants to find, add one
    return counter
def consonantfreq(word):
    """
    Description: This finds the freqency of consonants in the inputed word

    Args:
        word - the inputed name or word 

    Returns:
        rounded - the rounded consonant frequency in the word

    """
    counter = 0
    consonant = ("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM")
    for letter in word:
        if letter in consonant:                                     #for each letter in the word, if the letter is a consonant, add 1
            counter += 1
    amount = len(word)                                              #finds the amount of letters in the entire inputed word
    total = (counter/amount)                                        #total is the amount of total letters divided by the number of consonants in the word
    rounded = round(total, 2)*100                                   #take that total and round it to the hundreth, and multiply it by 100
    return rounded
def lower_case(word):
    """
    Description: This turns the user input into lowercase through ords
    
    Args:
        word - the inputed name or word 

    Returns:
        result - the inputed word all lowercase
    """
    result = ""
    for letter in word:
        letter_number = ord(letter)                                 #If the ordinal number for the letter
        if 65 <= letter_number <= 90:                               #Check if it's an uppercase letter
            letter_number += 32                                     # Convert to lowercase
        result = result + chr(letter_number)                        #add the letter to result and from the new word
        
    return result
def upper_case(word):
    """
    Description: This turns the user input into uppercase through ords
    
    Args:
        word - the inputed name or word 

    Returns:
        result - the inputed word all in uppercase
    """
    result = ""                                                     #Creates an empty list
    for letter in word:                                             #For every letter in the word
        letter_number = ord(letter)                                 #Find the ord of the letter
        if 97 <= letter_number <= 122:                              #If the ord is within these numbers which checks if it is lowercase
            letter_number -= 32                                     #Subtract 32 from the ord number which switches the letter to uppercase
        result = result + chr(letter_number)                        #Add each letter to the empty list which rewrites the word
    
    return result
def findhyphen(split_name):
    """
    Description: Finds if there is a hyphen in the last name
    
    Args:
        split_name - the name/word split into a list by spaces

    Returns:
        a boolean whether there is or isnt a hyphen 
    """
    hyphen = '-'                                                    
    lastname = split_name[-1]                                       #Sets the last index in split-name as last name
    for letter in lastname:                                         #For every letter in lastname
        if letter in hyphen:
            return True                                             #If one of the letters is a hypen, return true. 
def shuffleword(word):
    """
    Description: Shuffles the word or name randomly 
    
    Args:
        word - the name or word which the user inputed

    Returns:
        split_word - the word Arg just shuffled randomly
    """
    split_word = list(word)                                         #Turn the string into a list of each individual letter
    random.shuffle(split_word)                                      #Randomly shuffle the letters of the list using random function
    return split_word                                               #Return the shufled word 
def palindrome(split_name):
    """
    Description: Checks if the firstname is a palindrome 
    
    Args:
        split_name - the name or word which the user inputed split into a list

    Returns:
        A boolean
    """
    first = split_name[0]
    return first == first[::-1]
def prefix(name):
    """
    Description: Removes any prefix's that are apart of the users name 
    
    Args:
        name - the name/word that the user inputed

    Returns:
        split_name - the name split into a list by spaces without a prefix
    """
    prefix = ('Dr.', 'Mr.', 'Ms.', 'Mrs.', 'Miss.', 'Dr', 'Mr', 'Ms', 'Mrs', 'Miss', 'Sir', 'Esq', 'Esq.', 'Sir.', 'Ph.d', 'Ph.D')
    split_name = name.split(" ")                                    #Split the name by spaces                                         
    name_1 = split_name[0]                                          #Set the first index as name_1
    if name_1 in prefix:                                            #If the name is a prefix                                       
        return split_name[1:]                                       #Return the splitname without the first index
    else:
        return split_name
def initials(split_name):
    """
    Description: Finds the initials of the inputed name/word
    
    Args:
        split_name - the name inputed split by spaces

    Returns:
        result - the first letters or initials of each inputed name 
    """
    result = []                                                     
    for i in range(len(split_name)):                                #Starts a loop which checks each name in the list split_name
        val = split_name[i]                                         #val is a certain name
        letter = val[0]                                             #letter is the first letter of val
        result += letter                                            #Add the letter to the result list
    return result    
def prefixbool(name):
    """
    Description: Finds if the user inputed a prefix and returns a boolean
    
    Args:
        name - the inputed name

    Returns:
        boolean whether the name has a prefix or not 
    """
    prefix = ('Dr.', 'Mr.', 'Ms.', 'Mrs.', 'Miss.', 'Dr', 'Mr', 'Ms', 'Mrs', 'Miss', 'Sir', 'Esq', 'Esq.', 'Sir.', 'Ph.d', 'Ph.D')
    if name[0] in prefix:                                           #If the first index is a prefix
        return True
run = "yes" 
while run == "yes":                                                         #If the value run = yes, the while true will run unless it doesn't equal yes
    name = input("Please either enter your name or a word to further continue in the menu: ")
    counter = 0
    extrachar = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','|',';',':',',','.','?','>','<']
    for char in name:
        if char in extrachar:
            counter = counter =+ 1                                          #If any of the characters inputed are not a valid response, 1 will be added to the counter which will tell the program to restart 
    if counter > 0:
        print("Invalid! Please enter a name or word with out numbers or special characters!")
    else: 
        run = "grumpyviki"     
while True:
    num = ('0','1','2','3','4','5','6','7','8','9','10','11','12')
    split_name = prefix(name)                                               #This changes the split_name to name without a prefix
    names = len(split_name)
    print("---------------------------------------------------")
    for i in range(len(functions)):                                         #for each index or value in the functions list 
        val = functions[i]                                                  #Store in index/number of that value in val
        print(f"{i}: {''.join(val)}")                                       #Print the index/number of the specific function or value in the list, then print the corresponding function 
        print("---------------------------------------------------")
    choice = input("To run one of these functions, please enter the number corresponding to the function: ")
    try:                                                                    #This try and execpt sees if the users inputed response works, and if a value error occurs, it restarts 
        choice = int(choice)
        if choice == 0:
            if names == 1:                                                  #If the name has 1, 2 or 3 and more indexs or inputed name, certain functions will run
                print(f"Firstname: {firstname(split_name)}")
            if names == 2:
                print(f"Firstname: {firstname(split_name)}")
                print(f"Lastname: {lastname(split_name)}")
            if names >= 3:
                print(f"Firstname: {firstname(split_name)}")
                print(f"Middlename(s): {middlename(split_name)}")
                print(f"Lastname: {lastname(split_name)}")
        elif choice == 1:
            print(reverse(name))
        elif choice == 2:
            print(f"There are currently {vowels(name)} vowels in your word.")
        elif choice == 3:
            lettercounter = input("What letter would you like me to count?: ")
            print(counterletter(lettercounter, name))
        elif choice == 4:
            print(f"The consonant freqeuency of the word is {consonantfreq(name)}")
        elif choice == 5:
            print(lower_case(name))
        elif choice == 6:
            print(upper_case(name))
        elif choice == 7:
            print(' '.join(shuffleword(name)))
        elif choice == 8:
            print(findhyphen(split_name))
        elif choice == 9:
            print(palindrome(split_name))
        elif choice == 10:
            print(' '.join(initials(split_name)))
        elif choice == 11:
            print(prefixbool(name))
    except ValueError:
        print("Invalid number!")
    

