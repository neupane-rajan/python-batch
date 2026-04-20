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
print(data)


# 