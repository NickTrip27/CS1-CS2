import csv #Imports the microsoft excel functions
import random #Import the random functions
def has_digit(string): #Creates a function
    '''
Finds if a string has a digit in it 
Args:
string = the password entered by the user that will be scanned for a number
Returns:
a boolean which is either true or false 
    '''
    return any(char.isdigit() for char in string) #It returns boolean if there is any digit in the perameter
def has_special(string): #Creates a function
    '''
Finds if a string has a special character in it 
Args:
string = the password entered by the user that will be scanned for a number 
Returns:
a boolean which is either true or false 
    '''
    special = list("!@#$%^&*()-=_+{}|[]\:'<>?") #Makes a list for the variable special
    return any(char in special for char in string)#It returns boolean if there is any digit in the perameter

def print_account(websites, usernames, passwords, i): #Creates a function
    '''
Will print all the websites with their usernames and passwords at once 
Args:
Websites = a list with the websites entered
Usernames = a list with the usernames entered
Passwords = a list with the passwords entered
i = the index integer
Returns:
Prints all the entered Websites, Usernames, and Passwords
    '''
    print(f'''Website: {websites[i]}
Username: {usernames[i]}
Password: {passwords[i]}''')

def enter(websites, usernames, passwords): #Creates a function
    '''
Will run all the website, username, and password prompting to the user, saving every user input 
Args:
Websites = a list with the websites entered
Usernames = a list with the usernames entered
Passwords = a list with the passwords entered
Returns:
Prompts and saves the users websites, usernames, and passwords, or returns errors to the user
    '''
    websites.append(input("Enter your website: "))#Adds the users input into the list 
    usernames.append(input("Enter the username: "))#Adds the users input into the list 
    password_question = input("1. Enter the password 2. Generate a secure password  ")#Adds the users input into the list or the generated password
    if password_question == "1": 
         while True:
            password = input("Enter the password (Must have at least 8 character, 1 number, and 1 special character): ") 
            
            if has_digit(password) and len(password) > 8 and has_special(password): #If the users password follow the criteria, it is good
                passwords.append(password) #Adds the password into the list 
                break
            elif not has_digit(password): #If the password does not have a digit
                print("Password must have numbers!")
            elif len(password) < 8: #If the password does not have eight characters
                print("Password must be at least eight characters!")
            elif not has_special(password): #If the password does not have a special character 
                print("Password must have at least one special character!")
        
        
    else:
        secure = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ!@%$&*#+abcdefghijklmnopqrstuvwxyz1234567890") #A list of all the characters for the generated password
        random_psd = [] 
        for i in range(10): #for loop for 10 characters 
            random_psd.append(random.choice(secure))#Picks 10 random characters from the list 
        random.shuffle(random_psd)#Shuffles these characters
        random_psd = ''.join(random_psd)#Puts all the characters into one string
        print(f"This is your password: {random_psd}")
        passwords.append(random_psd)#Adds the generated password to the list
def main(): #Creates a function
    websites = []
    usernames = []
    passwords = []

    while True:
        enter(websites, usernames, passwords)

        keep_going = input("Keep going? yes/no: ")

        if keep_going == "no":
            break
    while True:
        mode = input("What would you like to do: 1. Enter a website and its username + password. 2. Print all exsisting username + passwords for each saved website. 3. Print an individual username + password for a specific website. 4. Change the username and password for a website. 5. Store in Excel Sheet 6. Stop Program ")

        if mode =="6":
            break

        elif mode =="1":
            enter(websites, usernames, passwords)

        elif mode =="2":
            for i in range(len(websites)):
                print_account(websites, usernames, passwords, i)
        elif mode =="3":
            web = input("Enter a website: ")

            if web in websites:
                i = websites.index(web)
                print_account(websites, usernames, passwords, i)
        elif mode =="4":
            web = input("Enter the website")

            if web in websites:
                i = websites.index(web)
                usernames[i] = input("New username: ")
                passwords[i] = input("New Password: ")

            else:
                print("Not in database!")
        elif mode == "5":
            columns = {}
            columns['websites'] = websites
            columns['usernames'] = usernames
            columns['passwords'] = passwords

            rows = zip(columns['websites'],columns['usernames'], columns['passwords'])

            with open('my_file.csv','w',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Websites', 'Usernames', 'Passwords'])
                writer.writerows(rows)
main()

