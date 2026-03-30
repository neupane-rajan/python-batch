# trying indexing in sets

s = {1, 2, 3, 4, 5, 6}
# print(s[0]) #indexing is not allowed in sets
y = [1, 2, 3, 4, 5, 6, 7, 8]
s.pop()
y.pop()
print(y)
print(s)


# creating sets
# empty set
a = {}
# print(type(a))
# note: {} creates a dictionary, not a set
# correct way to create a empty sets

s = set()
# print(type(s))
# print(s)

# creating set with value
a = {1, 2, 3}
# b = set([4,5,6]) # converting  list to sets
b = set("hello")
# print(b)
