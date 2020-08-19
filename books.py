import print_menu
import take_order
import total_bill
import datetime
def main():
    menu = {"Harry Potter":500, "Divergent":450, "Diary of a Wimpy Kids":450}
    print_menu.print_menu(menu)
    order_cart = take_order.take_order(menu)
    total = total_bill.total_bill(order_cart, menu)
    print("You ordered:", order_cart, "Your total is:$",total) 
    time = datetime.datetime.now()
    sales_log = open("sales.txt","a")
    sales_log.write(str(time))
    sales_log.write("Items:"+str(order_cart)+"\n")
    sales_log.write("Total:"+str(total)+"\n")
    sales_log.close()
    bill = open("bill.txt", "w")
    bill.write(str(time))
    bill.write("You have bought"+str(order_cart)+"\n")
    bill.write("You have paid:"+str(total)+"\n")
    bill.write("Thank your for shopping")
    bill.close()
main()
