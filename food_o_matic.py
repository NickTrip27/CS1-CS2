'''

'''

import random #Imports the random module which allows the code to read and take commands from the 'random' library
mains = ["Cheese pizza","Pepperoni Pizza","Margarita Pizza","Penne Pasta","Sapagetti Bolengnse","Cacio e Pepe","Filet Migion","Gnocchi","Chicken Parmesan","Veal"]#Creates our main course list along with 10 strings or dishes
seconds = ["with garlic bread","with bread sticks","with a side of soup","with a balsamic salad","with ceasar salad","with truffle fries","with a glass of wine","with parmesan cheese","with mozzarella sticks","with stuffed mushrooms"]#Creates our second course list with 10 strings or dishes
main_costs = [19.99,19.99,24.99,13.99,18.99,22.99,39.99,14.99,29.99,34.99]#Creates a list of variables paired through index's of the main course, assigning the price of eat individual main course meal
second_costs = [7.99,1.99,4.99,6.99,6.99,8.99,29.99,0.99,2.50,9.99]#Creates a list of variables paired through index's of the second course, assigning the price of eat individual second course meal

while True:
    try:
        number_of_items = int(input("Welcome to the Italian Food-O-Matic generator! How many items do you want? "))
        final = input(f"Your final order is {number_of_items}, is this correct?")

        if final != "no":
            for i in range(number_of_items):
                main = random.choice(mains)
                second = random.choice(seconds)
                print (f"{main} {second}. Total cost is ${round(main_costs[mains.index(main)] + second_costs[seconds.index(second)], 2)}")
            break
    except ValueError:
        print("Please enter a number")
        
