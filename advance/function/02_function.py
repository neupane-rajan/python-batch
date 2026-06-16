def add(a, b):
    return a + b


sum = add(100, 2)


# if sum < 100:
#     print("this is less than 100")
# else:
#     print("greater than hundrend")


def sum(a, b):
    sum = a - b
    return sum


# sub = sum(b=5, a=3)
# print(sub)


# check even or odd using function


def check_num(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


# number = int(input("enter a number: "))

# check_num(number)


# default parameter


def greeting(name="Random"):
    print(f"hello {name}, welcome back ")


greeting(name="niijo")


def citizen(country, district):
    print(country, district)


citizen("nepal", "kailali") #postional Argument: position matter
citizen(district="Kailai", country="Nepal")  # keyword arguments:position doesnot matter
