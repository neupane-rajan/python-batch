# tuple packing
# tuple packing means putting the values into tuple
# python automatically pack them and create tuple form it

t = 1, 2, 3, 4, 5, 6
# print(t)
# print(type(t))


# tuple unpacking
# unpacking  means extracting values from tuple

# t = (1, 2, 3, 4)
# a, b, c, d = t


# advance unpacking

t = (1, 2, 3, 4, 5)

# method 1
# a,*b,*b,*b=t
# method 2
*a,=t
# method 3
# a,*b,c=t
# print(a)
# print(b)
# print(c)
# a,b,*c=t\
a,*b,c,d=t
print(b)