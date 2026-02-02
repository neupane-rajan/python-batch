
username = "123"
psw1 = 123
psw2 = 345
user = input("enter your username")
psw = input("enter your psw")
if user== username:
    if psw == psw1:
        print("you have sucessfuly login as 123")
    elif psw == psw2:
        print("your have sucessfuly login as 345")
    else:
        print("wrong password")
else:
    print("you have entered worng username")

