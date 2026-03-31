from app.menu.view_menu import View
from app.order.take_order import Order
from app.booking.book_table import ManageTable
from app.billing.print_bill import generate_bill

class Staff:
    def staff_menu(self):
        while True:
            try:
                print(f"+{'-'*25}+")
                print("|       STAFF MENU        |")
                print(f"+{'-'*25}+")
                print("| 1. VIEW MENU            |")
                print("| 2. TAKE ORDER           |")
                print("| 3. BOOKING              |")
                print("| 4. BILLING              |")
                print("| 5. logout               |")
                print(f"+{'-'*25}+")

                option = input("\nplease select your choice-> ")
                if option.isdigit():
                    option = int(option)
                    if option == 1:
                        view_obj=View()
                        view_obj.view_data()

                    elif option == 2:
                        order_obj = Order()
                        order_obj.take_order()

                    elif option == 3:
                        table_obj = ManageTable()
                        table_obj.table_menu()

                    elif option == 4:
                        pass

                    elif option == 5:
                        print(f"Logout successful")
                        break
                    else:
                        print("invailid choice!!")
                else:
                    print(f"enter only digit!!")
            except Exception as e:
                print(f"{e}")
