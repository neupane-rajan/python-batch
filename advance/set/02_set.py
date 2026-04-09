# trying indexing in sets

s = {1, 2, 3, 4, 5, 6}
# print(s[0]) #indexing is not allowed in sets
y = [1, 2, 3, 4, 5, 6, 7, 8]
s.pop()
y.pop()
# print(y)
# print(s)


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


#adding elements 

# adding single elements at a time
set1 = {3,1,2}
set1.add(4)

# adding multiple item in sets
set1.update((20,6,100,8)) # non iterable item are not allowed we can only give iterable item here
# print(set1)


#Removing Elements
# remove() -> it gives error if not found or given empty
name ={"rajan","ram","dhirendra","Dipak"}
# name.remove("ram")
# discard() -> discard doesnot give any eror if item is not found
name.discard("suresh")
print(name)


# looping in sets

set2 = {1,2,3,4,5,6,7,8,9,10}
# for i in set2:
#     print(i)

print("4" in set2) #returs either true or false