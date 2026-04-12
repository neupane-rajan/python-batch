a = {1,2,3,4,5}
b = {1,2,3,4}
# union() or "|"
union = a.union(b,[1,2,3,4])
# print(union)



# intersection()
intersection = a.intersection(b)
# print(intersection)

# difference()
difference = a.difference(b)
# print(difference)


# symmetric_difference()
sm_dif = a.symmetric_difference(b)
# print(sm_dif)



# issubset()
# print(a.issubset(b))  # a b set ko subset hora
# print(b.issubset(a)) # b a set ko subset hora

# issuperset() yedi duitai set barabar xa vane duitai set ek arkako superset hunxan. yedi aauta set tulo xa vane tyo thulo wala set nai super set hunxa

# print(a.issuperset(b))
# print(b.issuperset(a))


# isdisjoint() -> yedi dui set bich kunai pani elements common hudaina vane teslai disjoint set vaninxa
print(a.isdisjoint(b))

# intersection_update()
# difference_update()
# symmetric_difference_update

# when to use operater and when to use method in sets