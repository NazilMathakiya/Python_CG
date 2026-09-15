# indexing
numbers = [10, 20, 30, 40]

print(numbers[0]) #10
print(numbers[2]) #30
print(numbers[-1]) #40

# slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4]) #[20, 30, 40]
print(numbers[:3])  #[10, 20, 30]
print(numbers[2:])  #[30, 40, 50]
print(numbers[::-1]) #[50, 40, 30, 20, 10]

# updating list
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)   #[10, 50, 30]

# add element
# append()
# Adds one element at the end.
numbers = [10, 20]

numbers.append(30)

print(numbers)  #[10, 20, 30]


# insert()
numbers.insert(1, 15)

print(numbers)  #[10, 15, 20, 30]


# extend()
numbers.extend([40, 50])

print(numbers) #[10, 15, 20, 30, 40, 50]


# Remove Element
# remove()
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)  #[10, 30, 20]

