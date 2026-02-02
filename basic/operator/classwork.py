# """
# Question 1
# •	Age ≥ 18 → check ID
# •	If ID available → Allow entry
# •	Else → Bring ID
# •	Else → Underage
# write a program to check the age of the user if age is greater than or equal to 18 then check for ID if ID is available allow entry else bring ID otherwise print underage

# """

# age = int(input("enter your age"))
# id = input("did you bring your id (yes/no)")
# if age>=18:
#     if id=="yes": 
#         print("you are allow to enter")
#     else:
#         print("bring your id")
# else:
#     print("underage")    

"""
Question 2
•	If it is raining
o	If you have umbrella → Go outside
o	Else → Stay home
•	Else → Go outside
write a program to check if it is raining or not if it is raining then check if you have umbrella if you have umbrella then go outside else stay home otherwise go outside
"""
check_raining = input("pani pardai xa kinai vana(yes/no):").lower()
check_umbrella = input("eaa ani umbrella xata(yes/no)")

if check_raining=="yes":
    if check_umbrella=="yes":
        print("eaa jau ta baira")
    else:
        print("teso bhaye umbrella lyayera au ani jane baira")
else:
    print("eaa jau ta baira")