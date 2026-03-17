# how to access tuple elements?
# we can excess element using same method as list method.

ex_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# positive index
elements = ex_tuple[3]
# print(elements)
# negative indexing
first_elements = ex_tuple[-2]
# print(first_elements)


"""
tuple slicing
syntax:
variable_name = [start:end]
variable_name = [start:end:step]
"""

t = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# sliced = t[0:4]
# sliced = t[0:7:2]
# sliced = t[::] # give all elements of tuple
sliced = t[:5]  # start form zero and end in 5 index
# print(sliced)


# tuple operation
# 1. concatenation means adding two tuple
a = (1, 2, 3)
b = (4,5)
c = a + b
# print(c)


# repetition
sam_tuple = (1,2)
rep_tuple = sam_tuple*3
# print(rep_tuple)

# checking or membership
a = (1, 2, 3)
# print(4 in a)





# built in function on tuples
#  len(),max(),min(),sum()
t = (10,20,30,40,50)
# print(len(t))
# print(max(t))
print(min(t))
print(sum(t))



# tuple methods
# tuple has only two method

# count()
# index()