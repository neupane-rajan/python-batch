# perfect number
# nuymber is perfetc if :
# the sum of its proper divisior excluding  itself is equal to the number

num = int(input("Enter a number="))
Sum_of_divisior = 0
if num == 0:
    print("please enter a number greater than zero")
else:
    for i in range(1, num):
        if num % i == 0:
            Sum_of_divisior = Sum_of_divisior + i
if Sum_of_divisior == num:
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect")
