import print_menu
import take_order
import total_bill
def main():
    menu = {"Marvel Series":500, "DC Series":450, "James Bond Series":450}
    print_menu.print_menu(menu)
    order_cart = take_order.take_order(menu)
    total = total_bill.total_bill(order_cart, menu)
    print("You ordered:", order_cart, "Your total is:$",total)
    print_time = datetime.datetime.now()
    sales_log = open("sales.txt","a")
    sales_log.write(str(print_time)+"\n")
    sales_log.write("Items:"+str(order_cart)+"\n")
    sales_log.write("Total:"+str(total)+"\n")
    sales_log.close()
    bill = open("bill.txt","w")
    bill.write(str(print_time)+"\n")
    bill.write("You have bought:"+str(order_cart)+"\n")
    bill.write("You have paid:"+str(total))
    bill.write("Thank you for visting.")
    bill.close()
main()