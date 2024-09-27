import random
mains = ["Cheese pizza","Pepperoni Pizza","Margarita Pizza","Penne Pasta","Sapagetti Bolengnse","Cacio e Pepe","Filet Migion","Gnocchi","Chicken Parmesan","Veal"]
seconds = ["with garlic bread","with bread sticks","with a side of soup","with a balsamic salad","with ceasar salad","with truffle fries","with a glass of wine","with parmesan cheese","with mozzarella sticks","with stuffed mushrooms"]
main_costs = [19.99,19.99,24.99,13.99,18.99,22.99,39.99,14.99,29.99,34.99]
second_costs = [7.99,1.99,4.99,6.99,6.99,8.99,29.99,0.99,2.50,9.99]

while True:
    try:
        number_of_items = int(input("Welcome to the Italian Food-O-Matic generator! How many items do you want? "))
        final = input(f"Your final order is {number_of_items}, is this correct?")

        if final != "no":
            used = []
            
            for i in range(number_of_items):
                main = random.choice(mains)
                second = random.choice(seconds)
                if main not in used:
                    used.append(main)
                    break
               
                    
                print (f"{main} {second}. Total cost is ${round(main_costs[mains.index(main)] + second_costs[seconds.index(second)], 2)}")
            break
    except ValueError:
        print("Please enter a number")
        
