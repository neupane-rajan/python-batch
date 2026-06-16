
# lamda function is a small nameless(anonymous) function
def square(x):
    return x*x
# print(square(5))


double  = lambda x:x*x
# print(double(5))


def add(a,b):
    return a+b

# print(add(1,2))


summ = lambda a,b:a+b
# print(summ(5,2))


# if else+ lambda

def check(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

num_check = lambda x:"even" if x%2==0 else "odd"

print(check(5))

# check which number is greater 

def check_greater(a,b):
    if a>b:
        return f"{a} is greatest"

    elif a==b:
        return f"{a} and {b} are equal"
    else:
        return f"{b} is greatest"


    
check_greater = lambda a,b:"a is greater than b" if a>b else "b is greater than a "
print(check_greater(2,4))

greatest = lambda a,b: "a is greater " if a>b else (b if b>a else "both are equal")

