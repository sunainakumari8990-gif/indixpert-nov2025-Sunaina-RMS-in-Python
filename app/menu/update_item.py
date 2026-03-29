from add_item import AddItem
import json
import os
path = os.path.join("app", "database", "item_data.json")

class Update:

    def item_update(self):
        try:
            if os.path.exists(path):
                with open(path, "r") as file:
                    try:
                        data = json.load(file)

                    except:
                        data = {
                            "morning": [],
                            "lunch": [],
                            "supper": [],
                            "dinner": []
                        }
            else:
                data = {
                    "morning": [],
                    "lunch": [],
                    "supper": [],
                    "dinner": []
                }

            category1 = "morning"
            category2 = "lunch"
            category3 = "supper"
            category4 = "dinner"

            while True:
                print(f"\n|{'-'*10}UPDATE MENU{'-'*10}|")
                print(f"| 1. morning item               |")
                print(f"| 2. lunch item                 |")
                print(f"| 3. supper item                |")
                print(f"| 4. dinner item                |")
                print(f"| 5. Back                       |")
                print(f"|{'-'*31}|\n")

                choice = input("please select your choice->> ")

                if choice.isdigit():
                    choice = int(choice)
                    if choice == 1:
                        print(f"\n  -------- {category1.upper()} ITEMS --------")
                        print(f"|{'-'*31}|")
                        for item in data[category1]:
                            print(f"| id: {item['id']}\t| Name: {item['name']}\t|")
                        print(f"|{'-'*31}|\n")

                        search_id = (input("please enter item id who you want to update: "))
                        
                        found = False
                        for item in data[category1]:
                            if item["id"] == search_id:

                                found = True
                                break
                        if found:
                            new_name = input("Enter new item name: ")
                            new_price1 = int(input("enter new item full price: "))
                            new_price2 = int(input("enter new item half price: "))
                            change_veg = input("veg (True\False): ")
                                
                            item["name"] = new_name
                            item["price1"] = new_price1
                            item["price2"] = new_price2
                            item["vagetarian"] = change_veg

                            with open(path, "w") as file:
                                json.dump(data, file, indent=4)
                            print("Item update successfully!")
                            continue

                        if not found:
                            print("invalid item name!!")
                            continue
                        

                    elif choice == 2:

                        print(f"\n  -------- {category2.upper()} ITEMS --------")
                        print(f"|{'-'*31}|")
                        for item in data[category2]:
                            print(f"| id: {item['id']}\t| Name: {item['name']}\t|")
                        print(f"|{'-'*31}|\n")

                        search_id = (input("please enter item id who you want to update: "))
                        
                        found = False
                        for item in data[category2]:
                            if item["id"] == search_id:

                                found = True
                                break
                        if found:
                            new_name = input("Enter new item name: ")
                            new_price1 = int(input("enter new item full price: "))
                            new_price2 = int(input("enter newitem half price: "))
                            change_veg = ("veg (True\False): ")
                                
                            item["name"] = new_name
                            item["price1"] = new_price1
                            item["price2"] = new_price2
                            item["vegetarion"] = change_veg

                            with open(path, "w") as file:
                                json.dump(data, file, indent=4)
                            print("Item update successfully!")
                            continue

                        if not found:
                            print("invalid item name!!")
                            continue


                    elif choice == 3:

                        print(f"\n  -------- {category3.upper()} ITEMS --------")
                        print(f"|{'-'*31}|")
                        for item in data[category3]:
                            print(f"| id: {item['id']}\t| Name: {item['name']}\t|")
                        print(f"|{'-'*31}|\n")

                        search_id = (input("please enter item id who you want to update: "))
                        
                        found = False
                        for item in data[category3]:
                            if item["id"] == search_id:

                                found = True
                                break
                        if found:
                            new_name = input("Enter new item name: ")
                            new_price1 = int(input("enter new item full price1: "))
                            new_price2 = int(input("enter new item half price2: "))
                            change_veg = input("veg (True\False): ")
                                
                            item["name"] = new_name
                            item["price1"] = new_price1
                            item["price2"] = new_price2
                            item["vegetarion"] = change_veg

                            with open(path, "w") as file:
                                json.dump(data, file, indent=4)
                            print("Item update successfully!")
                            continue

                        if not found:
                            print("invalid item name!!")
                            continue
                        

                    elif choice == 4:

                        print(f"\n  -------- {category4.upper()} ITEMS --------")
                        print(f"|{'-'*31}|")
                        for item in data[category4]:
                            print(f"| id: {item['id']}\t| Name: {item['name']}\t|")
                        print(f"|{'-'*31}|\n")

                        search_id = (input("please enter item id who you want to update: "))
                        
                        found = False
                        for item in data[category4]:
                            if item["id"] == search_id:

                                found = True
                                break
                        if found:
                            new_name = input("Enter new item name: ")
                            new_price1 = int(input("enter new item full price: "))
                            new_price2 = int(input("enter new item half price: "))
                            change_veg = input("veg (True\False): ")
                                
                            item["name"] = new_name
                            item["price1"] = new_price1
                            item["price2"] = new_price2
                            item["vegetarion"] = change_veg

                            with open(path, "w") as file:
                                json.dump(data, file, indent=4)
                            print("Item update successfully!")
                            continue

                        if not found:
                            print("invalid item name!!")
                            continue
                
                    elif choice == 5:
                        break

                    else:
                        print("invalid choice!!")
                else:
                    print("enter only digit!!")
    

        except Exception as e:
            print("Error:", e)





