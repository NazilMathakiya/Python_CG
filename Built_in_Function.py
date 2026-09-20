# len
arr = [10, 20, 30, 40]
print(len(arr))

# sum
arr = [10, 20, 30]
print(sum(arr))


# min and max
arr = [10, 5, 25, 8]

print(min(arr))
print(max(arr))


# abs
print(abs(-10))


# sorted
arr = [5, 2, 8, 1]
result = sorted(arr)
print(result)
print(arr)
# descending
sorted(arr, reverse=True)


# arr.sort() Changes the original list.
# sorted(arr) Creates a new sorted list.


# enumerate()
arr = [10, 20, 30]

for index, value in enumerate(arr):
    print(index, value)



# zip()
names = ["Nazil", "Rahul", "Jay"]
marks = [90, 80, 85]

for name, mark in zip(names, marks):
    print(name, mark)



# range()
names = ["Nazil", "Rahul", "Jay"]
marks = [90, 80, 85]

for name, mark in zip(names, marks):
    print(name, mark)



# reversed
arr = [1, 2, 3, 4]

for x in reversed(arr):
    print(x)



# any() and all()
arr = [False, False, True]
print(any(arr))  #any() → True if at least one is true.

arr = [True, True, True]
print(all(arr))   #all() → True if everything is true.


# type()
x = 10
print(type(x))


