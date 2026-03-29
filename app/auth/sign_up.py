import json
import datetime
import time
import os
import random
import re
import getpass

listdata = []

file_path = "app\\database\\userdata.json"
class people:
    def jsondata(self):
        if os.path.exists(file_path):
            with open(file_path,"r") as file:
                try:
                    old_data = json.load(file)
                except:
                    old_data = []

        else:
            old_data = []

        old_data.extend(listdata)
        with open(file_path, "w") as file:
            json.dump(old_data, file, indent=4)
        print("data save successful!!")

    def reg(self):
        try:
            while True:
                data = {}
                current_time = str(int(time.time()))
                current_date = datetime.datetime.now().strftime("%d/%m/%y")
                data["date"] = current_date
                data["id"] = current_time[-6:]

                # NAME
                while True:
                    try:
                        data["name"] = input("ENTER FULL NAME: ").strip().title()
                        if data["name"].replace(" ", "").isalpha() and 5 <= len(data["name"]) <= 30:
                            break
                        else:
                            print("only alphabet allowed (length 5-30)!")
                            continue
                    except Exception as e:
                        print(f"error: {e}")

                # ADDRESS
                while True:
                    try:
                        data["address"] = input("ENTER YOUR PRESENT ADDRESS: ").title()
                        if 3 <= len(data["address"]) <=50:
                            break
                        else:
                            print("address length must be 3-50!")
                            continue
                    except Exception as e:
                        print(f"error: {e}")

                # EMAIL
                while True:
                    try:
                        data["email"] = input("ENTER EMAIL ID: ")
                        pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
                        if re.match(pattern, data["email"]):
                            break
                        else:
                            print("invalid email format!!")
                            continue
                    except Exception as e:
                        print(f"error: {e}")

                # DUPLICATE EMAIL CHECK
                with open(file_path,"r") as file:
                    old_data = json.load(file)

                email_exist = False
                for user in old_data:
                    if user["email"] == data["email"]:
                        email_exist = True
                        break

                if not email_exist:
                    while True:
                        try:
                            print("----verify email----")
                            email_send_otp = str(random.randint(100000,999999))
                            print("send otp on your email:", email_send_otp)

                            e_otp = input("ENTER OTP: ")
                            if email_send_otp != e_otp:
                                print("invalid otp!!")
                                continue
                            print("email verify successful!!")
                            break

                        except Exception as e:
                            print(f"error: {e}")

                if email_exist:
                    print("email already registered!!")
                    break
      

                # PASSWORD
                while True:
                    try:
                        data["password"] = getpass.getpass("SET A PASSWORD: ")
                        if  6 <= len(data["password"]) <= 15:
                            break
                        else:
                            print("password length invalid(6-15)!!")
                            continue
                    except Exception as e:
                        print(f"error: {e}")
                # MOBILE
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

                while True:
                    try:
                        print("----verify mobile number----")

                        mobile_send_otp = str(random.randint(100000,999999))
                        print("send otp on your mobile:", mobile_send_otp)
                        m_otp = (input("ENTER OTP: "))
                        if mobile_send_otp == m_otp:
                            break
                        else:
                            print("invalid otp!!")
                            continue

                    except Exception as e:
                        print(f"error: {e}")

                print("mobile number verify successful!!")
                data["role"] = "staff"
                listdata.append(data)
                print("REGISTRATION SUCCESSFUL!!")
                break

        except Exception as e:
            print(f"error: {e}")


