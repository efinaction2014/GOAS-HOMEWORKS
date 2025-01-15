# 8 kyu
# even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# 8 kyu
# Reversed Strings
def solution(string):
    return string[::-1]
# 8 kyu
# Find the smallest integer in the array
def find_smallest_int(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest
# 8 kyu
# Multiply
def multiply(a, b):
    return a * b