data = {
    "name": "dhirendra",
    "age": 17,
    "course": "python",
    "address": "purba lamki",
    "test": "123",
}
# pop: remove specific items
removed_item = data.pop("name")
print(data)
print(removed_item)


# # del
removed_item2 = del data["age"]

print(removed_item2)
