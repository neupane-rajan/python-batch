# a nested loop is one loop inside another loop
# outerloop -> row
# inner loop -> column
# outer loop  decide the number of rows
# inner loop decide the number of columns
# structure or syntax for nested loop
"""
for i in range(x):       #   outerloop
    for j in range(y):   # inner loop
        statement
"""

# for i in range(4):
#     for j in range(5):
#         print("*",end=" ")
#     print()

for i in range(1,4):
    for j in range(1,8):
        print(i,j)
    