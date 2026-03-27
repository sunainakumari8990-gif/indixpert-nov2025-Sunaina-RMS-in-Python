from add_item import Manage
from view_menu import View
from update_item import Update
from delete_item import Delete

import json
import os
class Item:
    def menu(self):

        try:
            while True:
                print("--------------------")
                print("1. ADD ITEM")
                print("2. VIEW MENU")
                print("3. UPDATE ITEM")
                print("4. DELETE ITEM")
                print("5. EXIT")
                print("--------------------\n")

                option = input("please select option->>")
                if option.isdigit():
                    option = int(option)
                    if option == 1:
                        obj = Manage()
                        obj.menu()                      
                        
                    elif option == 2:
                        view_obj=View()
                        view_obj.view_data()
                        
                    elif option == 3:
                        update_obj = Update()
                        update_obj.item_update()
                
                    elif option == 4:
                        deleteobj = Delete()
                        deleteobj.delete_item()
                        
                    elif option == 5:
                        print("EXIT!!")
                        break
                    else:
                        print("invalid option!!")
                else:
                    print("enter only digit!!")
                    
        except Exception as e:
            print(f"Error: {e}")

obj_manu = Item()
obj_manu.menu()
        