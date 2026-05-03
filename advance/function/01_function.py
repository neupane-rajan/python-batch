# function:
# A function is a block of reusable code that perform a specific task

# syntax:
# def function_name():
# code
# def-> used to create a function or define the function
# functionName-> used for calling function and it should be meaning fullw


# def greeting():
#     print("hello welcome to python batch")


# greeting()  # calling fucntion


# # add


# def add():
#     print(5 + 2)


# add()

# parameter: varible that is inside the fucntion
# argument: actual value that is passed during calling the function


def greeting(name1, name2):
    print(f"hello {name1}")
    print(f"hello i am {name2}")


n1 = input("enter your name: ")

n2 = input("enter your firend name: ")
greeting(n1, n2)
