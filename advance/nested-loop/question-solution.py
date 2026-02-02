"""
1 1 1
2 2 2
3 3 3

1 2 3
2 3 4
3 4 5

*
* *
* * *
* *
*

1
2 3
4 5 6
7 8 9 10


A
A B
A B C
A B C D

1
2 1
3 2 1
4 3 2 1

* * * *
*     *
*     *
* * * *

*
* *
*   *
*     *
* * * * *


1
2 4
3 6 9
4 8 12 16

*   *
  *
*   *
  *
*   *


1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16





"""

# for i in range(1,4):
#     for j in range(1,4):
#         print(i+j-1,end=" ")
#     print()

"""
*
* *
* * *
* *
*

"""
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(2, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
1
2 3
4 5 6
7 8 9 10

"""
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


"""
A
A B
A B C
A B C D

"""

for i in range(1, 5):
    ch = ord("A")
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

# alternative method
strings = "A B C D"
for i in range(1, 5):
    print(strings[: i * 2].strip())
    print()

"""
1
2 1
3 2 1
4 3 2 1
"""

for i in range(1, 5):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

"""
* * * *
*     *
*     *
* * * *

"""
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#  alternative method
row = 4
col = 4
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            print("*", end=" ")
        else:
            print("", end="")
    print()


"""
*
* *
*   *
*     *
* * * * *
"""

rows = 5
for i in range(1, i + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(rows):
    print("*", end=" ")


"""
1
2 4
3 6 9
4 8 12 16
"""
for i in range(1, 5):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

"""
*   *
  *
*   *
  *
*   *
"""
for i in range(5):
    for j in range(5):
        if (i % 2 == 0 and (j == 0 or j == 4)) or (i % 2 == 1 and j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
"""

print(
    """
1 2 3 4
2 4 6 8
     
"""
)
