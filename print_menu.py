#Printing Menu
def print_menu(menu):
    for item, price in menu.items():
        show_menu = print(item,":$",price)
    return show_menu
