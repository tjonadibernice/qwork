list_order = []
list_qty = []
list_price = []
list_type = []
paid = []
grandtotal = 0
def save():
    print("-" * 100)
    print("-" * 100)
    print("Please enter the quantity you'd like to order.")
    qty = int(input())
    list_order.insert(len(list_order), food)
    list_qty.insert(len(list_qty), qty)
    list_price.insert(len(list_price), price)
    if (order_choice != 3):
        list_type.insert(len(list_type), 1)
    else:
        list_type.insert(len(list_type), 0)
    print("-" * 100)
    print("-" * 100)
    print("Your order has been added.")

def order():
    global food
    global price
    global order_choice
    print("-" * 100)
    print("-" * 100)
    print("ORDER")
    print("What would you like to order?")
    order_choice = 1
    while (order_choice != 0):
        print("-" * 100)
        print("-" * 100)
        print("Please choose and enter a number.")
        print("1. Breakfast Set")
        print("2. Lunch Set")
        print("3. Other Services")
        print("0. Back to Main Menu")
        order_choice = int(input())
        if (order_choice == 1):
            bfast_choice = 1
            while (bfast_choice != 0):
                print("-" * 100)
                print("-" * 100)
                print("1. Set 1\tRoti Prata with Coffee\t(RM 10)")
                print("2. Set 2\tSandwich with Tea\t(RM 10)")
                print("3. Set 3\tPorridge with Coffee\t(RM 10)")
                print("0. Back to Order")
                bfast_choice = int(input())
                if (bfast_choice == 1):
                    food = "B. Set 1"
                    price = 10
                    save()
                elif (bfast_choice == 2):
                    food = "B. Set 2"
                    price = 10
                    save()
                elif (bfast_choice == 3):
                    food = "B. Set 3"
                    price = 10
                    save()
                elif (bfast_choice == 0):
                    break
                else:
                    print("-" * 100)
                    print("-" * 100)
                    print("Invalid entry.")
                    print("Please enter a valid number.")
        elif (order_choice == 2):
            lunch_choice = 1
            while (lunch_choice != 0):
                print("-" * 100)
                print("-" * 100)
                print("1. Set 1\tNasi Lemak with Coffee\t(RM 6)")
                print("2. Set 2\tBelacan Nasi Goreng with Tea\t(RM 7)")
                print("3. Set 3\tMongolia Fish Rice with Coffee\t(RM 8)")
                print("0. Back to Order")
                lunch_choice = int(input())
                if (lunch_choice == 1):
                    food = "L. Set 1"
                    price = 6
                    save()
                elif (lunch_choice == 2):
                    food = "L. Set 2"
                    price = 7
                    save()
                elif (lunch_choice == 3):
                    food = "L. Set 3"
                    price = 8
                    save()
                elif (lunch_choice == 0):
                    break
                else:
                    print("-" * 100)
                    print("-" * 100)
                    print("Invalid entry.")
                    print("Please enter a valid number.")
        elif (order_choice == 3):
            others_choice = 1
            while (others_choice != 0):
                print("-" * 100)
                print("-" * 100)
                print("1. 10by10ft\tTent\t(RM 400)")
                print("2. 50 Pcs\tChairs\t(RM 100)")
                print("3. 10 Pcs\tTables\t(RM 80)")
                print("4. 10 Pcs\tTable Clothes\t(RM 20)")
                print("0. Back to Order")
                others_choice = int(input())
                if (others_choice == 1):
                    food = "Tent"
                    price = 400
                    save()
                elif (others_choice == 2):
                    food = "Chairs"
                    price = 100
                    save()
                elif (others_choice == 3):
                    food = "Tables"
                    price = 80
                    save()
                elif (others_choice == 4):
                    food = "Table Clothes"
                    price = 20
                    save()
                elif (others_choice == 0):
                    break
                else:
                    print("-" * 100)
                    print("-" * 100)
                    print("Invalid entry.")
                    print("Please enter a valid number.")
        elif (order_choice == 0):
            break
        else:
            print("-" * 100)
            print("-" * 100)
            print("Invalid entry.")
            print("Please enter a valid number.")

def report():
    report_choice = 1
    while (report_choice != 0):
        print("-" * 100)
        print("-" * 100)
        print("Please choose and enter a number.")
        print("1. Show invoice.")
        print("2. Show summary of orders and payments made.")
        print("0. Back to Main Menu.")
        report_choice = int(input())
        if (report_choice == 1):
            if (grandtotal == 0):
                print("You haven't checked the total amount to be paid.")
                print("Please proceed to check first.")
                break
            else:
                print("-" * 100)
                print("-" * 100)
                print ("report")
                print("=================================")
                print("-------------INVOICE-------------")
                print("=================================")
                print("            DELI CAFE")
                print("    Rumah Keusahawan ENT3 TPM")
                from datetime import datetime
                now = datetime.now()
                Year = now.year
                Month = now.month
                Day = now.day
                Hour = now.hour
                Minute = now.minute
                Second = now.second
                print("Date:", Month,"/" , Day ,"/", Year)
                print("Time:", Hour, ":", Minute, ":", Second)
                print("-" * 100)
                print("Type\tName\t\tQty\tAmount")    
                for report_count in range(0, len(list_order)):
                    if list_type[report_count] == 1:
                        amount = list_qty[report_count] * list_price[report_count]
                        print("Meal\t"+str(list_order[report_count])+"\t"+str(list_qty[report_count])+"pc(s)\tRM "+str(amount))
                    else:
                        amount = list_qty[report_count] * list_price[report_count]
                        print("Others\t"+str(list_order[report_count])+"\t"+str(list_qty[report_count])+"pc(s)\tRM "+str(amount))
                print("Subtotal: %.2f" % subtotal)
                print("Discount: %.2f" % discount)
                print("GST: %.2f" % GST)
                print("Service Charge: %.2f" % Ser_Charge)
                print("Grand Total: %.2f" % grandtotal)
        elif (report_choice == 2):
            if (paid == []):
                print("No payment has been made.")
                print("Please proceed to the payment first.")
                break
            else:
                print("-" * 100)
                print("-" * 100)
                print("Type\tName\t\tQty\tAmount")    
                for report_count in range(0, len(list_order)):
                    if list_type[report_count] == 1:
                        amount = list_qty[report_count] * list_price[report_count]
                        print("Meal\t"+str(list_order[report_count])+"\t"+str(list_qty[report_count])+"pc(s)\tRM "+str(amount))
                    else:
                        amount = list_qty[report_count] * list_price[report_count]
                        print("Others\t"+str(list_order[report_count])+"\t"+str(list_qty[report_count])+"pc(s)\tRM "+str(amount))
                print("The total amount to be paid: %.2f" % paid[0])
                print("The total amount paid: %.2f" % paid[1])
                print("The balance: %.2f" % paid[2])
                print("The type of payment: ", paid[3])
        elif (report_choice == 0):
            break
        else:
            print("-" * 100)
            print("-" * 100)
            print("Invalid entry.")
            print("Please enter a valid entry.")
    
def payment ():
    global paid
    global subtotal
    global GST
    global discount
    global Ser_Charge
    global grandtotal
    payment_choice = 1
    while (payment_choice != 0):
        print("-" * 100)
        print("-" * 100)
        print("Please choose and enter a number.")
        print("1. Show the total amount to be paid.")
        print("2. Make payment.")
        print("0. Back to Main Menu.")
        payment_choice = int(input())
        if (payment_choice == 1):
            total_food = 0
            total_others = 0
            for payment_count in range (0, len(list_order)):
                if ((list_type[payment_count])== 1):
                    total_food = total_food + (list_price[payment_count]) * (list_qty[payment_count])
                else: 
                    total_others = total_others + (list_price[payment_count]) * (list_qty[payment_count])
            disc_count = 0
            discount = 0
            for a in range (0, len(list_order)):
                disc_count = disc_count + int(list_qty[a])
                if (disc_count >= 10 and disc_count <= 25):
                    discount = (total_food * 5/100)
                elif (disc_count >= 26 and disc_count <= 50):
                    discount = (total_food * 10/100)
                elif (disc_count >= 51 and disc_count <= 100):
                    discount = (total_food * 15/100)
                elif (disc_count >= 100):
                    discount = (total_food * 20/100)
            subtotal = total_food + total_others
            GST = (6/100) * (subtotal - discount)
            Ser_Charge = 5/100 * (subtotal - discount)
            grandtotal = subtotal - discount + GST + Ser_Charge
            print("-" * 100)
            print("-" * 100)
            print("Subtotal: %.2f" % subtotal)
            print("Discount: %.2f" % discount)
            print("GST: %.2f" % GST)
            print("Service Charge: %.2f" % Ser_Charge)
            print("Grand Total: %.2f" % grandtotal)
        elif (payment_choice == 2):
            if (grandtotal == 0):
                print("You haven't checked the total amount to be paid.")
                print("Please proceed to Show the total amount to be paid option.")
                break
            else:
                print("-" * 100)
                print("-" * 100)
                print("Which payment methods do you want to choose?")
                print("1.Cash \n2.Credit \n3.Debit\n")
                pay_methods = int(input())
                change = 0
                pin = 0
                if (pay_methods == 1):
                    cash_count = 0
                    while (cash_count == 0):
                        x = int(input("Enter the total paid"))
                        if (x < grandtotal):
                            print("-" * 100)
                            print("-" * 100)
                            print("The amount you enter is less than the grand total.")
                            print("Please enter the sufficient amount.")
                        else:
                            change = (x - grandtotal)
                            print("-" * 100)
                            print("-" * 100)
                            print("The balance of your change is: %.2f" % change)
                            paid = []
                            paid.insert(len(paid), grandtotal)
                            paid.insert(len(paid), x)
                            paid.insert(len(paid), change)
                            paid.insert(len(paid), "Cash")
                            break
                elif (pay_methods == 2):
                    print("-" * 100)
                    print("-" * 100)
                    print("Your transaction has been successfully made.")
                    paid = []
                    paid.insert(len(paid), grandtotal)
                    paid.insert(len(paid), grandtotal)
                    paid.insert(len(paid), 0)
                    paid.insert(len(paid), "Credit")                
                elif (pay_methods == 3):
                    pin = int(input("Enter your pin"))
                    print("-" * 100)
                    print("-" * 100)
                    print("Your transaction has been deducted from your bank account.")
                    paid = []
                    paid.insert(len(paid), grandtotal)
                    paid.insert(len(paid), grandtotal)
                    paid.insert(len(paid), 0)
                    paid.insert(len(paid), "Debit")                  
                else:
                    print("-" * 100)
                    print("-" * 100)
                    print("Invalid entry.")
                    print("Please enter a valid entry.")
                print("-" * 100)
                print("DELI CAFE")
                print ("\nThank You")
        elif (payment_choice == 0):
            break
        else:
            print("-" * 100)
            print("-" * 100)
            print("Invalid entry.")
            print("Please enter a valid entry.")
service = 1
while (service != 0):
    print("-" * 100)
    print("-" * 100)
    print("\t\t###### ","   ######","   #     ","   #######")
    print("\t\t#     #","   #     ","   #     ","      #   ")
    print("\t\t#     #","   #     ","   #     ","      #   ")
    print("\t\t#     #","   ######","   #     ","      #   ")
    print("\t\t#     #","   #     ","   #     ","      #   ")
    print("\t\t#     #","   #     ","   #     ","      #   ")
    print("\t\t###### ","   ######","   ######","   #######")

    print("Welcome to Deli Catering")
    print("Please choose and enter a number")
    print("1. Order")
    print("2. Payment")
    print("3. Report")
    print("0. Exit")
    service = int(input())
    if (service == 1):
        order()
    elif (service == 2):
        payment()
    elif (service == 3):
        report()
    elif (service == 0):
        exit()
    else:
        print("-" * 100)
        print("-" * 100)
        print("Invalid entry.")
        print("Please enter a valid entry.")
