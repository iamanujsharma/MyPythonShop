list = ("Books","Movies", "Food")
for item in list:
    print(item)

    
choice = input("What do you want: - ")
if choice.upper() == "BOOKS":
    exec(open("books.py").read())
elif choice.upper() == "MOVIES":
    exec(open("movies.py").read())
elif choice.upper() == "FOOD":
    exec(open("food.py").read())
else:
    ("Sorry, we don't have your item")
