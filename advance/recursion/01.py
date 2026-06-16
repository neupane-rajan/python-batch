# def countdown(n):

#     if n == 0:
#         print("countdown stop here ")
#         return
#     print(n)
#     countdown(n - 1)


# print(countdown(5))


# factorial
# 5!
# 4!*5
# 3!*4*5
# 2!*3*4*5
# 1!*2*3*4*5


def factorial(n):
    if n == 4:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
