import json
import os

path = os.path.join("app", "database", "item_data.json")

class AddItem:
    # -------- ADD ITEM --------
    def add_item(self, item_type):
        item = {
            "id": input("Enter id: "),
            "name": input("Enter item name: "),
            "price1": int(input("Enter full price: ")),
            "price2": int(input("enter half price: ")),
            "vegetarian": input("Veg (true/false): ")
        }

        if os.path.exists(path):
            with open(path, "r") as file:
                try:
                    data = json.load(file)

                except:
                    data = {
                        "morning": [],
                        "noon": [],
                        "evening": [],
                        "night": []
                    }
        else:
            data = {
                "morning": [],
                "noon": [],
                "evening": [],
                "night": []
            }

        data[item_type].append(item)
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"{item_type} item added successfully!")

# -------- MENU CONTROL --------
class Manage:
    def __init__(self):
        self.obj = AddItem()
        

    def menu(self):
        while True:
            print("\n======== MENU ========")
            print("1. Add Morning Item")
            print("2. Add Noon Item")
            print("3. Add Evening Item")
            print("4. Add Night Item")
            print("5. Back")

            choice = input("Enter choice: ")
            if choice.isdigit():
                choice=int(choice)
                if choice == 1:
                    self.obj.add_item("morning")

                elif choice == 2:
                    self.obj.add_item("noon")

                elif choice == 3:
                    self.obj.add_item("evening")
                    
                elif choice == 4:
                    self.obj.add_item("night")
        
                elif choice == 5:
                    break

                else:
                    print("Invalid choice!")



