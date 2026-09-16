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

# pop()
numbers = [10, 20, 30]

x = numbers.pop()

print(x)
print(numbers)   #30 , [10, 20]
# specific index
numbers.pop(0)


# clear()
numbers.clear()


# del
numbers = [10, 20, 30]

del numbers[1]

print(numbers)  #[10, 30]


# Searching
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 not in numbers)  #True , True


# important list method
numbers = [30, 10, 40, 20]

numbers.sort()
print(numbers)  #[10, 20, 30, 40]

# descending
numbers.sort(reverse=True)

# reverse
numbers.reverse()

# copy
new_list = numbers.copy()

#index
numbers.index(30)

# count
numbers.count(20)

# traversing
numbers = [10, 20, 30]

for num in numbers:
    print(num)
# with index
for i in range(len(numbers)):
    print(i, numbers[i])


# nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])   #[1, 2, 3] , 6

# Built-in-function
numbers = [10, 20, 30, 40]

print(len(numbers))  #4
print(sum(numbers))  #100
print(max(numbers))  #40
print(min(numbers))  #10


# List assignment vs copy
a = [1, 2, 3]
b = a

b.append(4)

print(a)   #[1, 2, 3, 4]

# copy
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)    #[1, 2, 3] , [1, 2, 3, 4]


