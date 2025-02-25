'''
Nicholas Triplett

orders (each individual function)
1. Prompt user for a name or word
2. Pick the function and find its characteristics
3. Plan how to rewrite the function
4. Rewrite the function and test it on the prompt
5. Document the function and then move onto the rest
6. Try to do all 18, document everythig

'''
import random
functions = ['Print your Firstname, Middlename(s), and Lastname', 'Reverse your name/word', 'Find the number of vowels in your name/word', 'Count a certain amount of letters in your name/word', 'Find the consonant frequency in your name/word', 'Convert your name/word into lowercase', 'Convert your name/word into uppercase', 'Shuffle the letters in your name/word', 'Find if there is a hyphen in your lastname or word', 'Find if your firstname or word is a palindrome', 'Print your initials', 'Find if your name has a title/distinction']
print("Hello and welcome to the WhatsinaName menu!")
def firstname(split_name):
    """
    This finds the firstname of the entered name 

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
    result = ""
    for letter in word:
        letter_number = ord(letter)
        if 65 <= letter_number <= 90:  # Check if it's an uppercase letter
            letter_number += 32  # Convert to lowercase
        result = result + chr(letter_number)
        
    return result
def upper_case(word):
    result = ""
    for letter in word:
        letter_number = ord(letter)
        if 97 <= letter_number <= 122:
            letter_number -= 32
        result = result + chr(letter_number)
    
    return result
def findhyphen(split_name):
    hyphen = '-'
    lastname = split_name[-1]
    for letter in lastname:
        if letter in hyphen:
            return True
def shuffleword(word):
    split_word = list(word)
    random.shuffle(split_word)
    return split_word
def palindrome(split_name):
    first = split_name[0]
    return first == first[::-1]
def prefix(name):
    prefix = ('Dr.', 'Mr.', 'Ms.', 'Mrs.', 'Miss.', 'Dr', 'Mr', 'Ms', 'Mrs', 'Miss', 'Sir', 'Esq', 'Esq.', 'Sir.', 'Ph.d', 'Ph.D')
    split_name = name.split(" ")
    names = len(split_name)
    name_1 = split_name[0]
    if name_1 in prefix:
        print(split_name[1:])        
        return split_name[1:]
    else:
        return split_name
def initials(split_name):
    result = []
    for i in range(len(split_name)):
        val = split_name[i]
        letter = val[0]
        result += letter
    return result    
def prefixbool(name):
    prefix = ('Dr.', 'Mr.', 'Ms.', 'Mrs.', 'Miss.', 'Dr', 'Mr', 'Ms', 'Mrs', 'Miss', 'Sir', 'Esq', 'Esq.', 'Sir.', 'Ph.d', 'Ph.D')
    if name[0] in prefix:
        return True
run = "yes" 
while run == "yes":
    name = input("Please either enter your name or a word to further continue in the menu: ")
    counter = 0
    extrachar = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','|',';',':',',','.','?','>','<']
    for char in name:
        if char in extrachar:
            counter = counter =+ 1     
    if counter > 0:
        print("Invalid! Please enter a name or word with out numbers or special characters!")
    else: 
        run = "grumpyviki"     
while True:
    num = ('0','1','2','3','4','5','6','7','8','9','10','11','12')
    split_name = prefix(name)
    names = len(split_name)
    print("---------------------------------------------------")
    for i in range(len(functions)):
        val = functions[i]
        print(f"{i}: {''.join(val)}")
        print("---------------------------------------------------")
    choice = input("To run one of these functions, please enter the number corresponding to the function: ")
    try:
        choice = int(choice)
        if choice == 0:
            if names == 1:
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


