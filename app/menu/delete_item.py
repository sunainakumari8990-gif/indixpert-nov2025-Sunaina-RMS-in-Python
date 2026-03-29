from add_item import AddItem
import json
import os

path = os.path.join("app", "database", "item_data.json")

class Delete:

    def delete_item(self):
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


            print(f"+{'-'*31}+")
            print(f"|\t  DELETE MENU\t\t|")
            print(f"|{'-'*31}|")
            print(f"| 1. morning item                |")
            print(f"| 2. lunch item                  |")
            print(f"| 3. supper item                 |")
            print(f"| 4. dinner item                 |")
            print(f"+{'-'*31}+\n")

            category = input("Enter category (morning/lunch/supper/dinner): ").lower()
            if category not in data:
                print("Invalid category!")
                return
            if not data[category]:
                print("No items in this category!")
                return

            print(f"\n-------- {category.upper()} ITEMS --------")
            print(f"|{'-'*28}|")
            for item in data[category]:
                print(f"| id: {item['id']}  | Name: {item['name']}    |")
            print(f"|{'-'*28}|\n")

            item_name = input("Enter item name to delete: ")

            found = False
            for item in data[category]:
                if item["name"] == item_name:
                    data[category].remove(item)
                    found = True
                    break
            if found:
                with open(path, "w") as file:
                    json.dump(data, file, indent=4)
                print(f" item delete successfully!")

            if not found:
                print("Item not found in this category!")

        except Exception as e:
            print("Error:", e)



