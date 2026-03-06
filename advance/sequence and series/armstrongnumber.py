num = int(input("enter a number"))
temp = num
digits = len(str(num))
sum = 0
while temp > 0:
    d = temp % 10
    sum = sum + (d**digits)
    temp = temp // 10
if sum == num:
    print("armstrong number")
else:
    print("no an  armstrong")
