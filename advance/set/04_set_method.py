# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5}
# union() or "|"
# union = a.union(b,[1,2,3,4])
# print(union)


# intersection()
# intersection = a.intersection(b)
# print(intersection)

# difference()
# difference = a.difference(b)
# print(difference)


# symmetric_difference()
# sm_dif = a.symmetric_difference(b)
# print(sm_dif)


# issubset()
# print(a.issubset(b))  # a b set ko subset hora
# print(b.issubset(a)) # b a set ko subset hora

# issuperset() yedi duitai set barabar xa vane duitai set ek arkako superset hunxan. yedi aauta set tulo xa vane tyo thulo wala set nai super set hunxa

# print(a.issuperset(b))
# print(b.issuperset(a))


# isdisjoint() -> yedi dui set bich kunai pani elements common hudaina vane teslai disjoint set vaninxa
# print(a.isdisjoint(b))


"""
print(f"b before intersection update:", b)
# intersection_update()
b.intersection_update(a)
# y = a.intersection(b)
print("value of a:", a)
# print(x, y)
print("b after intersection_update", b)
# difference_update(): it removes comment elements from the orginal set.
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
# print("b before: ", b)
# b.difference_update(a)
# print("b after: ", b)
"""

# symmetric_difference_update : keep elements that are non common in  given sets
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
b.symmetric_difference_update(a)
print(a)
print(b)
# when to use operater and when to use method in sets
