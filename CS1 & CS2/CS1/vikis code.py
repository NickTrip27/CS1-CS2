movie_list = "A river runs through it", "Elf", "Grown Ups", "Night at the Museum"

River = "Brad Pitt", "Craig Sheffler"
Elf = "Will Ferrel"
Grown_up = "Adam Sandler"
Night = "Steve Carrell"
while True:
    movie = input("Enter a movie")

    if movie in movie_list:
        print ("You have entered a correct movie!")
        break
    elif movie!= movie_list:
        print ("Not in list")
def new_func():
    actor = input("Enter a main character in the movie!: ")
    return actor

while True:
    actor = new_func()
    if actor == River or Elf or Grown_up or Night:
        print("WOHOO")
        break
    else:
        print("try again")




    