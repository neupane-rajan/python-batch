# Dictionary in python is a collection of key-value paris.
# word = key , meaning = value

# creating empty dictionary
# student_details = {}  # <class 'dict'>
# print(type(student_details))
# student_details = dict()  # <class 'dict'>

# yedi dictionay hamle duplicate key diyeu vane jun key chai last ma dinxam tesko value update hunxa
# student_details = {
#     "name": "Rajan",
#     "name": 22,
#     "course": "python",
#     "name": "changed name",
# } not god
student_details = {"name": "Dipak", "age": 16, "course": "python", "class": 9}
# print(student_details)

# important note:
# 1 key must be unique
# values can be anything(string,integer,list, even another dictionary)

# creating a dictionary

# method using {}

# data = {"a": 1, "b": 2}
d = {"1": "hello"}
# method using dict()
data = dict(name="rajan", age=22, course="python")

# in above
# name is converted into key
# = conveted into :
# "rajan" = conveted in value

# print(data)


# Accessing Values in dictionary
data = {
    "name": "dhirendra",
    "age": 17,
    "course": "python",
    "address": "purba lamki",
    "test": "123",
}

# 1.Method
# if key doesnot exist in dictionary then it will throw us KeyError
# print(data["address"])

# 2.Method :if key doesnot exist in dictionary then it will return None
# .get()
# print(data.get("name"))

# Adding key and value to the dictionary
# data["school"] = "USS"

# updating dictionary
# data["name"] = "Bharat"  # in this way we can update our dictionary


# Removing Items

# pop: remove specific items and return the removed value
# data.pop("name")
# popitem(): remove last item from dictionary
# data.popitem()

# del: remove specific items. its doesnt return any value and this is keyword not a method
# del data["age"]

# clear(): clear everything form dictionary and return empty dictionary
data.clear()

print(data)
