# set
# A collection of unique elements is called sets
# it is unordered(no fixed position/index)
# it is denoted or written using {value1,value2,value3} if it is empty then it is dictonary not a set

my_set = {1, 2, 3, 4, 5, 6}
# print(type(my_set))

# we cannot put any duplicate item in set
# a set is like magical bag that remove the duplicates item automatically.
num = {2, 3, 4, 5, 6, 6, 9, 9, 1, 8, 2}
# print(num)

# why is set unorder?
# elemtes are stored based on hash value

# hash value
# hash value is a number that python creates internally for each object

s = {10, 20, 30}
# hash(10)->store
# hash(20)->store
# hash(30)-> store
s.add(20)
# has(20)-> check if it already exits-> dont add


# print(hash("hi"), hash("ai"))
# both are different so they have different hash value

# set is not always in assending order
s = {1, 10, 3, 7}
print(s)

# print(hash("a"), hash("a"))
