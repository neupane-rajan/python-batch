""" a list is a collection of multiple values stored in a single variable
features of list
-- list is denoted by "[]"
1. list is a data type same like integer, string, boolean, none and so on
1. collection of multiples value
2. list can store multiple data types
3. list is mutable (can be changed)


my_list = [1,2,3,4,5] # integer type list
class_B_Student_Name = ["ramesh","dhirendra","suresh","dipak","rajan"] # string type list 
float_list = [1.5,2.5,3.5,4.5,5.5] # float type list
bool_list = [True, False, True, False] # boolean type list
none_list = [None, None, None] # none type list
mix_list = [1,"ramesh",3.5,True,None] # mixed data type list
"""


# creating a empty list and it is denoted by "[]"
num = []
num1 = list()
# print(empty_list,empty_list1)
# print(type(empty_list))

"""
every item in a list has a position number called index
index starts from 0

my_list = ["apple", "rajan", "cherry", "date", "elderberry"]
# index:        0        1         2        3          4
# negative index: -5      -4        -3       -2         -1

# accessing list items using positive index
first_item_of_list = my_list[0]
last_item_of_list = my_list[-1]
print(f"first_list_element={first_item_of_list},\nthird_list_element={second_item_of_list}")

# accessing list using negative index
print(f"neg_index_item={my_list[-4]}")
"""

"""
list slicing variable_name[start:end]
start= included 
end = excluded
list = [10,20,30,40,50,60,70,80,90,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150]
sub =list[-2:]
#sub_list = list[0:4]
# sub_list = list[:3] # its start from 0 and just end before  index 3  :10,20,30
# sub_list1 = list[3:] # its start from 3 and it goes to end of the list :40,50,60
sub_list2=list[:]  # give all the number from list 
print(sub_list2)"""


list = [10,20,30,40,50,60,70,80,90,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,1433]
sub =list[-2:]
print(sub)
# student_name_by_roll = ["ram","shyam","hari","gita","sita","laxman","urmi"]

# print(student_name_by_roll[])