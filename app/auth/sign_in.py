import json
import os
listdata=[]
class user:

    def login(self):
        file_path = "app\\database\\userdata.json"
        if os.path.exists(file_path):
            with open(file_path,"r") as file:
                try:
                    json_read = json.load(file)
                except:
                    json_read = []
        else:
            json_read = []

        user_email = input("please enter your email id: ")
        user_password = input("please enter your password: ")
        

        found = False
        for i in json_read:
            if i["email"] == user_email and i["password"] == user_password:
                print("login successful!!")
                found = True
                break

        if not found:
            print("user not found!!")
