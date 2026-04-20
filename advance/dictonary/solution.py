"""
1.Create a dictionary using dictionary comprehension where numbers 1 to 5 are keys and their squares are values.
2.Create a dictionary where numbers 1 to 5 are keys and their cubes are values.
3.Create a dictionary from a list ["apple", "banana", "cat"] where keys are words and values are their lengths.
4.Create a dictionary using numbers 1 to 10 where only even numbers are keys and values are their squares.
5.Create a dictionary from {"a":1, "b":2, "c":3} by swapping keys and values. keep
"""

number_square = {i: i**2 for i in range(1, 6)}
print(number_square)
