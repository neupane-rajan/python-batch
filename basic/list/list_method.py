"""# list is a mutable data structure in Python
#           0         1        2        3
fruits = ["apple","banana","cherry","jackfruit"]
# replace the value of item
fruits[0]="litchi"
print(fruits)
"""

"""
# adding items to the list

# append() : append is used to add value at the end
num = [1,2,3,4,5,6]
num.append(7)
print(num)

# insert() add item at specific index
# sample.insert(index,value)
class_11 =["ram","shyam","hari","gita",["ram","shyam","hari"]]
print(class_11[-2])


"""

# pop,remove,sort,
#  pop is used to remove item from specific index but if we do not provide any value it removes last item by default
"""student_name = ["ram","shyam","hari","bharat","dhirendra","sirish"]
student_name.pop(3)
print(student_name)

# remove us used to remove item by given value.

student_name.remove("ram")
print(student_name)



# sort is used to sort the list in ascending order or in decending order using reverse = True
#reverse is used to reverse the list



string_data = ["banana","apple","cherry","mango","kiwi"]
# string_data.sort()
string_data.reverse()
print(string_data)
"""

# # len
# num = [1,2,3,4,5,6,7,8,9,10]

# list_num_lengt = len(num)
# print(list_num_lengt)

# # in use in list for checking item present in the list or not
# cloth_list = ["red-shirt","black-tshirt","shoes","hat"]
# check_clothes= "hat" in cloth_list
# print(check_clothes)

# # iterating list using for loop
# numList = [10,20,30,40,50,60,70,80,90]
# for i in range(1,20,3):
#     print(i)