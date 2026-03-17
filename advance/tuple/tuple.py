# tuple is an ordered collection of elements that cannot be changed.
# tuple is immutable, it means we cannnot modify or change the value of tuple.

# variable_name = (value1,value2,value3............,valueN)
# properties of tuple:
# 1. ordered
# 2. Immutable
# 3. can store different data types
# 4. tuple is faster and consume less memory than list

# student_name = ("rajan","dhirendra","bharat","dipak",'a','a','j','a')

# print(student_name.index("rajan"))
# print(student_name.count('a'))

# print(student_name.append(1)) we cannot use this method in tuple as tuple is immutable


# create an empty tuple
# using ()
# empty_tuple = ()

# using tuple() function
# empty_tuple = tuple()
# print(type(empty_tuple))
# print(empty_tuple)

# creating tuple by putting different values

# method 1-> using()
# num = (1,2,3,4,5,6,7)
# print(num)
# (1, 2, 3)

# method 2 -> with out parenthesis : python automatically creates tuple here.
# t = 1,2,3
# print(t)
# print(type(t))

# method 3: using tuple() function
# new_tuple = tuple([1,2,3,4,5,6,7,8])
# print(type(new_tuple))


# mistake that we repeate while declearing tuple

t = (4)
print(type(t))

# correct way to put element if we have only

t = (4,)
print(type(t))
