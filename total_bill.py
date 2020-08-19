#calculation_bill
def total_bill(order_cart, menu):
    total = 0
    for item in order_cart:
        total = total + menu[item]
    return total