"""
*
* *
* * *
* *
*

1
2 3
4 5 6
7 8 9 10

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


n = input("enter a number")
digit = len(n)
sum = 0
for d in n:
    sum = sum + int(d) ** digit
if sum == int(n):
    print("armstrong")
else:
    print("not an armostrong number")
