#Set operations(important)

# union(combination of two or more than two sets)
# union is denoted by "|" symbol in python but in math we often use "U"
a = {1,2,3}
b = {4,3,5}
union = a|b
# print(union) #{1,2,3,4,5}

# intersection(common elements btw any two or more than two sets)
# intersection is denoted by "&"
intersection = a & b
# print(f"intersection: {intersection}")
# difference
# difference is denoted by "-"
# when we wrote a-b we got only elements that are unique in A set
# we we wrote b-a we got only element that are unique in B set
difference = a-b
differenceb=b-a
# print(f"difference of a: {difference}\n difference of b: {differenceb}")
# symmetric difference
symmetric_difference = a^b
# print(symmetric_difference)


# we can make our set immutable by using unique function
frozen_set = frozenset({1,2,3,4,5})
# now this is immutable like tuple
# we cannot add or remove any item
# frozen_set.add(1)
# print(frozen_set)


# set comprehension
newSet = {x for x in range(5)}
print(newSet)