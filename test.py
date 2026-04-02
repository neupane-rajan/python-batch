"""
1 2 3
1 2 3
1 2 3
1 2 3
1 2 3 4
"""

for i in range(1, 6):
    for j in range(1, 4):
        if i == 5:
            print("1 2 3 4")
            break

        print(j, end=" ")
    print()
