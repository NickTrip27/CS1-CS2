'''
Name: Nicholas Triplett

Description: Acts as a postal service and calculates the cost of shipping certain items. The program takes in the diameters of the item and the too+from destinations, and calculates a cost depending on all five of these variables.

Bugs: None

Features: None

Sources: W3 Schools - https://www.w3schools.com/ - Code Academy - https://www.codecademy.com/

Log: 1.0 (initial release)
'''

def get_type(length,height,thickness):
    """
    Finds the type of size of mail.

    Args:
        Length(int): The length of the item.
        Height(int): The height of the item.
        thickness(float): The thickness or width of the item 

    Returns:
        Str: The mailing type based on the given size. 

    Raises:
        ValueError: If there are negative numbers, or letters.

    """
     #Each if/elif scans each measurment to find if it is within certain numbers
     #If one of these if/elifs matches, it will return the type of mail
    if 3.5<=length<=4.25 and 3.5<=height<=6 and .007<=thickness<=.016:     
        return "Regular Post Card"
    elif 4.25<=length<=6 and 6<=height<=11.5 and .007<=thickness<=.015:
        return "Large Post Card"
    elif 3.5<=length<=6.125 and 5<=height<=11.5 and .016<=thickness<=.25:
        return "Regular Envelope"
    elif 6.125<=length<=24 and 11<=height<=18 and .25<=thickness<=.5:
        return "Large Envelope"
    elif length+2*height+2*thickness<=84:
        return "Package"
    elif 84<length+2*height+2*thickness<130:
        return "Large Package"
    else:
        print("Unmailable")
def get_zone(zip):
    """
    Finds the zone of the entered zip code

    Args:
        zip(int): The zip code entered by the user 

    Returns:
        Int: A number depending on the entered zip code 

    Raises:
        ValueError: If there are negative numbers, or letters.

    """
    #Each if/elif scans the entered zip code to find which zones the number is in 
    #If one of the if/elif finds the zip is within certain zipcodes throught greater or less than, it will return the zone
    if zip > 1 and zip < 6999:
        return 1
    elif zip > 7000 and zip < 19999:
        return 2
    elif zip > 20000 and zip < 35999:
        return 3
    elif zip > 36000 and zip < 62999:
        return 4
    elif zip > 63000 and zip < 84999:
        return 5
    elif zip > 85000 and zip < 99999:
        return 6
def cost(size,zone):
    """
    Determines the cost it will take for the user to ship their item

    Args:
        size(str): The mail type found earlier in get_type
        zone(int): The distance of zones the mail will travel determined by the difference of the zip zones

    Returns:
        int: A number which is the cost of the shipping

    Raises:
        ValueError: If there are negative numbers, or letters.

    """
    #Each if/elif finds the mail type and applies a calculation that is influenced by the zone 
    #It returns a final cost of the shipping 
    if size == 'Regular Post Card':
        return .20+.03*zone
    elif size == 'Large Post Card':
        return .37+.03*zone
    elif size == 'Regular Envelope':
        return .37+.04*zone
    elif size == 'Large Envelope':
        return .60+.05*zone
    elif size == 'Package':
        return 2.95+.25*zone
    elif size == 'Large Package':
        return 3.95+.35*zone
    

def main ():
    
    
    print("Welcome to the GCDS Post-Office!")       #Welcome the user to the post office
    data = input("Please enter your length, height, thickness(width), the postal code you are shipping from, the postal code you are shipping to: ")
                                                    #Gets the data by storing the users input 
    while True:                                     #Starts a while true that will scan the users input for incorrect formating
        
    
    #break input into piece  4,4,.009,02893,08516   
    
        data = data.split(",")                      #Splits the users input by each comma into individual indexs
        
        for item in data:                           #Checks each index in data as 'item' 
            if item.isalpha():                      #if one of these indexs inputed is a letter(In the alphabet) it will tell the user they used incorrect formatting, and will re ask for their data
                data = input("Incorrect format, you entered a letter! Please enter your length, height, thickness(width), the postal code you are shipping from, the postal code you are shipping to(all in numbers please): ")
                continue                            #Allows the while true to continue running and re scan the new data
          
        if len(data) != 5:                          #Checks if the users did not enter 5 inputs
            data = input("Incorrect format! Please enter your length, height, thickness(width), the postal code you are shipping from, the postal code you are shipping to(all in numbers please): ")
                                                    #If there is not 5 indexs, it will tell the user they incorrectly formatted and re asks for their data 
            continue                                #Allows the while true to continue running and re scan the new data

        else: 
        
            break                 
    length = int(data[0])                           #Creates a variable 'lenght' that stores the value of the users first input as an integer 
    height = int(data[1])                           #Creates a variable 'height' that stores the value of the users second input as an integer
    thickness = float(data[2])                      #Creates a variable 'thickness' that stores the value of the users third input as a float
    zipfrom = int(data[3])                          #Creates a variable 'zipfrom' that stores the value of the users fourth input as an integer
    ziptoo = int(data[4])                           #Creates a variable 'ziptoo' that stores the value of the users fifth input as an integer
    
    
    distance = abs(get_zone(zipfrom - get_zone(ziptoo)))                    #Creates a variable 'distance', that calls the getzone function, and subtracts the returns. The abs makes sure the return is a positive integer
    ship_type = get_type(length,height,thickness)                           #Creates a variable 'ship_type', that calls the get_type function and sets the returned mailing type into the variable
    final = cost(ship_type,distance)                                        #Creates a variable 'final' that calls the cost function and sets the returned cost to the variable
    final = str(final)                                                      #Makes the final variable which stores the final cost a string
    final = final.lstrip("0")                                               #Because the variable final is now a string, the function lstrip is set to remove the leading zero
    
    print(f"You will need a {ship_type}, and the cost will be: ${final}")   #Prints to the user what their final mail type is, and their final shipping cost by printing the ship_type and final variables
    
    
    
main()                                              #Runs the main function 


