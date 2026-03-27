from add_item import AddItem
import json
import os
path = os.path.join("app", "database", "item_data.json")

class View:
    def __init__(self):
        self.obj = AddItem()

    def view_data(self):

        try:
            with open(path, "r") as file:
                data = json.load(file)

            category1 = "morning"
            category2 = "noon"
            category3 = "evening"
            category4 = "night"

            print(f"\n          -------- {category1.upper()} ITEMS --------\n")
            print(f"+{'-'*63}+")
            print(f"| ID \t| ITEM \t\t| FULL Rs. | HALF Rs.\t| VEGETARIAN    |")
            print(f"|{'-'*63}|")
            for item in data[category1]:
                print(f"| {item['id']}\t| {item['name']}  \t| {item['price1']}\t   | {item['price2']} \t| {item['vegetarian']}  \t|")
            print(f"+{'-'*63}+\n")

            
            print(f"\n          -------- {category2.upper()} ITEMS --------\n")
            print(f"+{'-'*63}+")
            print(f"| ID \t| ITEM \t\t| FULL Rs. | HALF Rs.\t| VEGETARIAN    |")
            print(f"|{'-'*63}|")
            for item in data[category2]:
                print(f"| {item['id']}\t| {item['name']}\t| {item['price1']}\t   | {item['price2']}  \t| {item['vegetarian']}\t\t|")
            print(f"+{'-'*63}+\n")


            print(f"\n          -------- {category3.upper()} ITEMS --------\n")
            print(f"+{'-'*63}+")
            print(f"| ID \t| ITEM \t\t| FULL Rs. | HALF Rs.\t| VEGETARIAN    |")
            print(f"|{'-'*63}|")
            for item in data[category3]:
                print(f"| {item['id']}\t| {item['name']}\t| {item['price1']}\t   | {item['price2']}  \t| {item['vegetarian']}\t\t|")
            print(f"+{'-'*63}+\n")
    
            
            print(f"\n          -------- {category4.upper()} ITEMS --------\n")
            print(f"+{'-'*63}+")
            print(f"| ID \t| ITEM \t\t| FULL Rs. | HALF Rs.\t| VEGETARIAN    |")
            print(f"|{'-'*63}|")
            for item in data[category4]:
                print(f"| {item['id']}\t| {item['name']}  \t| {item['price1']}\t   | {item['price2']}  \t| {item['vegetarian']}\t\t|")
            print(f"+{'-'*63}+\n")


        except Exception as e:
            print("Error:", e)
            

