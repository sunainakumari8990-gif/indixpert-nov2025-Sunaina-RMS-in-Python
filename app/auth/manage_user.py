from sign_in import user 
from sign_up import people

class usermanage:

    def usermenu(self):
        try:
            while True:

                print(f"+{'-'*40}+")
                print(f"|       SUPER FAMOUS RESTAURENT          |")
                print(f"+{'-'*40}+\n")
                print(f"+{'-'*30}+")
                print(f"| 1. LOGIN                     |")
                print(f"| 2. SIGN UP                   |")
                print(f"| 3. EXIT                      |")
                print(f"+{'-'*30}+")

                option=(input("please select your choice->"))
                if option.isdigit():
                    option = int(option)

                    if option==1:
                        login_obj=user()
                        login_obj.login()

                    elif option==2:
                        signup_obj=people()
                        signup_obj.reg()
                        signup_obj.jsondata()

                    elif option==3:
                        print("EXIT!")
                        break
                    else:
                        print("invalid ! ")
                else:
                    print("invalid choice!!")
                    continue
        except Exception as e:
            print(f"{e}")



manageuser=usermanage()
manageuser.usermenu()

