#Taking Order
def take_order(menu):
    order_cart = []
    order = ""
    order = input("What would you like to order(Q for Quit):-")
    while order.upper() != "Q":
        if order in menu:
            order_cart.append(order)
        else:
            print("Menu doesn't exist")
        order = input("Anything would you like to add(Q to Quit:-")
    return order_cart