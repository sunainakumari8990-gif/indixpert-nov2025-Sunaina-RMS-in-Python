import json
import os
import datetime
import time

path = "app\\database\\booking_data.json"

class ReserveTable:

    # load data
    def load_data(self):
        if os.path.exists(path):
            with open(path, "r") as file:
                try:
                    return json.load(file)
                except:
                    return []
        return []

    # save data
    def save_data(self, data):
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

    #book table
    def booking_info(self):
        data = {}

        #-----id & date-----
        current_time = str(int(time.time()))
        today = datetime.datetime.now().strftime("%d/%m/%y")
        data["current_date"] = today
        data["id"] = current_time[-6:]

        #-----name-------
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
        #----mobile----
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
        #-----address-----
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

    
        #----booking date----
        while True:
            booking_date = input("PLEASE ENTER BOOLING DATE(DD-MM-YYYY): ")
            try:
                datetime.datetime.strptime(booking_date, "%d-%m-%Y")
                data["booking_date"] = booking_date
                break
            except:
                print("invalid date formate")
                continue

        #----TIME SLOT----
        while True:
            print("please select time slot-> ")
            print("1. 08:00 AM - 11:00 AM")
            print("2. 11:00 AM - 02:00 PM")
            print("3. 02:00 PM - 05:00 PM")
            print("4. 05:00 PM - 08:00 PM")

            option = int(input("please select your option-> "))

            if option == 1:
                data["time_slot"] = "08:00 AM - 11:00 AM"
                break
            elif option == 2:
                data["time_slot"] = "11:00 AM - 02:00 PM"
                break
            elif option == 3:
                data["time_slot"] = "02:00 PM - 05:00 PM"
                break
            elif option == 4:
                data["time_slot"] = "05:00 PM - 08:00 PM"
                break
            else:
                print("invalid time slot!!")
                continue
        
        #----table-----
        table_no = [101, 102, 103, 104, 105]
        total_seat = [4, 6, 2, 8, 4]
        fare = [50, 40, 60, 40, 50]
        old_data = self.load_data()

        print(f"available table:")
        for i in range(len(table_no)):
            available = total_seat[i]

            for booking in old_data:
                if (booking["table"] == table_no[i] and
                    booking["booking_date"] == data["booking_date"] and
                    booking["time_slot"] == data["time_slot"]):

                    available -= booking["seat"]

            print(f"table no: {table_no[i]} (available seats: {total_seat[i]})")
        table = int(input("please select table numer: "))
        seats = int(input("enter number of seats: "))

        
        found = False
        for i in range(len(table_no)):
            if table_no[i] == table:
                # data["table"] = table
                found = True
                available = total_seat[i]

                for booking in old_data:
                    if (booking["table"] == table and
                        booking["booking_date"] == data["booking_date"] and
                        booking["time_slot"] == data["time_slot"]):

                        available -= booking["seat"]

                if seats > available:
                    print("Not enough seats available!")
                    return

                # save data
                data["table"] = table
                data["seat"] = seats
                data["total_seat"] = total_seat[i]
                data["price_per_seat"] = fare[i]

                #bill calculation
                subtotal = seats * fare[i]
                gst = subtotal * 0.12
                total = subtotal + gst

                data["subtotal"] = subtotal
                data["gst"] = gst
                data["total_bill"] = total

                print(f"booking successful!!")
                print(f"subtotal: {subtotal}")
                print(f"GST (12%): {gst}")
                print(f"total bill: {total}")
                break
        if not found:
            print("Invalid table number!")
            return 

        old_data.append(data)
        self.save_data(old_data)

    def cancel_booking(self):
        booking_id = input(f"ENTER BOOKING ID: ")
        data = self.load()

        new_data = [b for b in data if b["id"] != booking_id]
        if len(data) == len(new_data):
            print("Booking not found!")
        else:
            self.save_data(new_data)
            print("Booking cancelled!")

    # view booking
    def view(self):
        data = self.load_data()
        if not data:
            print("No bookings found!")
            return
    
        print("\n------ ALL BOOKINGS ------")
        for b in data:
            print(f"""
        ID: {b['id']}
        Name: {b['name']}
        Table: {b['table']}
        Seats: {b['seat']}
        Date: {b['booking_date']}
        Time: {b['time_slot']}
        Total Bill: {b['total_bill']}
        --------------------------
        """)

class ManageTable:
    def table_menu(self):
        obj = ReserveTable()
        while True:
            print(f"+{'-'*25}+")
            print(f"|       TABLE MENU        |")
            print(f"+{'-'*25}+")
            print(f"| 1. Book Table           |")
            print(f"| 2. Cancel Booking       |")
            print(f"| 3. View Booking         |")
            print(f"| 4. Exit                 |")
            print(f"+{'-'*25}+")

            choice = input("\nEnter choice: ")
            if choice.isdigit():
                choice = int(choice)

                if choice == 1:
                    obj.booking_info()
                elif choice == 2:
                    obj.cancel_booking()
                elif choice == 3:
                    obj.view()
                elif choice == 4:
                    print("Thank you!")
                    break
                else:
                    print("invalid choice!")
            else:
                print("enter only digit!!")
        
table_obj = ManageTable()
table_obj.table_menu()


