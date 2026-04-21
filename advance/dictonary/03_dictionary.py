# Nested Dictionary

students = {
    "student1": {"name": "Dipak", "age": "16"},
    "student2": {"name": "Dhirendra", "age": "18"},
    "student3": {"name": "Bharat", "age": "18"},
    "student4": {"name": "Shirish", "age": "16"},
}

shirish_info = students["student4"]["age"]
# print(dipak_info)


# Dictionary Comprehension
squares = {x: x**4 for x in range(1, 6)}
# print(squares)


names = ["ram", "shyam", "hari", "krishna", "sita"]
# data = {name: len(name) for name in names}

data = {name: len(name) for name in names}
# print(data)

# Advanced Concepts

# 1.copy()
# it help us to avoids modifying original dictionary
# new_dict = students.copy()
# print(new_dict)

# 2. formkeys()
x = ["a", "b", "c", "d"]
y = [0, 0, 0, 0]
y = dict.fromkeys(x, y)

print(y)

