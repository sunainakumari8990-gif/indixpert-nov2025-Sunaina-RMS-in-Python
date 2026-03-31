import json
import os
import datetime
import time

path = os.path.join("app", "database", "item_data.json")
path2 = os.path.join("app", "database", "order_data.json")
class Order:
    
    def load_items(self):
        if os.path.exists(path):
            with open(path, "r") as file:
                try:
                    return json.load(file)

                except Exception as e:
                    print(f"{e}")
                    
        else:
            data = {}
    def load_orders(self):
        if os.path.exists(path2):
            with open(path2, "r") as file:
                try:
                    return json.load(file)
                except:
                    data = {}
        
        else:
            data = {}

    def save_order(self, order):
        orders = self.load_orders()
        orders.append(order)

        with open(path2, "w") as file:
            json.dump(orders, file, indent=4)

    def take_info(self):
        data = {}
        current_time = str(int(time.time()))
        current_date = datetime.datetime.now().strftime("%d/%m/%y")
        data["date"] = current_date
        data["id"] = current_time[-6:]

        #name
        while True:
            try:
                data["name"] = input("ENTER CUSTOMER NAME: ").title()
                if data["name"].replace(" ", "").isalpha() and 5 <= len(data["name"]) <= 30:
                    break
                else:
                    print("only alphabet allowed (length 5-30)!")
                    continue
            except Exception as e:
                print(f"error: {e}")
        #mobile
        while True:
            try:
                data["mobile"] = input("ENTER MOBILE NUMBER: ")
                if data["mobile"].isdigit() and len(data["mobile"]) == 10:
                    break
                else:
                    print("invalid mobile number!!")
                    continue
                                    
            except Exception as e:
                print(f"error: {e}")
    #address
        while True:
            try:
                data["address"] = input("ENTER CUSTOMER'S PRESENT ADDRESS: ").title()
                if 3 <= len(data["address"]) <=50:
                    break
                else:
                    print("address length must be 3-50!")
                    continue
            except Exception as e:
                print(f"error: {e}")
        return data
        
    def select_category(self, data):
        categories = list(data.keys())

        print("\n---- Categories ----")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        while True:
            try:
                choice = int(input("Select category: "))
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                    #break
                else:
                    print("Invalid choice!")
            except:
                print("Enter number only!")

        #SHOW MENU
    def show_menu(self, items):
        print("\n------ MENU ------")
        print(f"+{'-'*63}+")
        print(f"| ID \t| ITEM \t\t| FULL Rs. | HALF Rs.\t| VEGETARIAN    |")
        print(f"|{'-'*63}|")
        for item in items:
            print(f"| {item['id']}\t| {item['name']}  \t| {item['price1']}\t   | {item['price2']}  \t| {item['vegetarian']}\t\t|")
        print(f"+{'-'*63}+\n")

    def find_item(self, items, user_input):
        for item in items:
            if item["id"] == user_input or item["name"].strip().lower() == user_input.lower():
                return item
        return None

     # -------- TAKE ORDER --------
    def take_order(self):
        data = self.load_items()

        if not data:
            print("No data found!")
            return

        customer = self.take_info()
        order_list = []
        total_bill = 0

        while True:
            category = self.select_category(data)
            items = data[category]
            self.show_menu(items)
            user_input = input("Enter Item ID/Name (q to quit): ")
            if user_input.lower() == "q":
                break
            item = self.find_item(items, user_input)
            if not item:
                print("Item not found!")
                continue
            # Quantity
            while True:
                try:
                    qty = int(input("Enter Quantity: "))
                    if qty > 0:
                        break
                    else:
                        print("Invalid quantity!")
                except:
                    print("Enter number only!")

            # Size
            while True:
                size = input("Enter Size (half/full): ").lower()
                if size == "full":
                    price = item["price1"]
                    break
                elif size == "half":
                    price = item["price2"]
                    break
                else:
                    print("Invalid size!")

            subtotal = price * qty
            total_bill += subtotal

            order_list.append({
                "category": category,
                "item": item["name"],
                "size": size,
                "qty": qty,
                "price": price,
                "subtotal": subtotal
            })

            print(f"Added: {item['name']} x{qty} ({size}) = ₹{subtotal}")

        # -------- BILL --------
        print("\n------ FINAL BILL ------")
        for o in order_list:
            print(f"{o['category']} | {o['item']} | {o['qty']} x {o['price']} = ₹{o['subtotal']}")

        print("-" * 40)
        print(f"TOTAL BILL = ₹{total_bill}")
        print("-" * 40)

        # -------- SAVE --------
        customer["orders"] = order_list
        customer["total_bill"] = total_bill

        self.save_order(customer)

        print("Order Saved Successfully")


order_obj = Order()
order_obj.take_order()


