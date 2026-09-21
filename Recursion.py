# basic recursion
def count(n):
    if n == 0:
        return

    print(n)
    count(n - 1)

count(5)



# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))



# sum of number
def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)

print(total(5))



# find the sum of list
def array_sum(arr, index):
    if index == len(arr):
        return 0

    return arr[index] + array_sum(arr, index + 1)

arr = [10, 20]

print(array_sum(arr, 0))   #100
