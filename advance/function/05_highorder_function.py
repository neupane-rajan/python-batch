"""function can be called as high order  function if it
-> take function as argument
-> return function
"""

# example


def greeting():
    print("hello student")


def hig_ord(func):
    func()


# hig_ord(greeting)


# passing function as a arguments


def addition(num1, num2):
    return num1 + num2


def calculate(func, x, y):
    return func(x, y)


# print(calculate(addition, 10, 20))


def signin():
    print("you have successfully signed in")


def logout():
    print("you have logged out successfully")


# highorder function
def message(func):
    func()


# check = input("do you want to logged out or signed in(l/s)")

# if check == "l":
#     message(logout)
# else:
#     message(signin)


# returning function


def outside():

    def inside():
        print("this is inside the function")

    return inside()


# outside()


# map

# syntax

# map(function,iterable)
# iterable = list, tuple , string, dict , set


nums = [1, 2, 3, 4, 5]

square = map(lambda x: x**2, nums)
# print(list(square))


name = ["ram", "shyam", "hari"]

up_case = map(str.upper, name)
# print(list(up_case))
# print(list(up_case))


# filter()
# we use filter when removing items

# example

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))


# enumerate

x = ["x","y","z"]
y = enumerate(x)
print(tuple(y))