# Arbitrary Argument(*args)


def total(*nums):
    return nums


# x = total(1, 2, 3, 4, 5)
# print(type(x))


# Arbitrary keyword arguments


def id_card(**info):
    print(info)


# id_card(name="rajan", age="22")


# local variable


def add():
    x = 1
    print(x)


# add()
# x=2
# print(x)


# global variable

# num = 100


def displaynumber():
    num = 101
    print(num)


# displaynumber()

# print(num)

# modifying global
x = 5


def modify():
    global x
    x = 10
    print(x)


print(x)
modify()
print(x)
