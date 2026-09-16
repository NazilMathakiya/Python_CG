# A tuple is an ordered collection like a list, but it is immutable (cannot be changed).
numbers = (10, 20, 30, 40)
names = ("Arman", "Rahul", "Jay")

# Single element tuple needs a comma:
t = (10,)

# Without comma, it is not a tuple:
t = (10)
print(type(t))   # int


# indexing and slicing
t = (10, 20, 30, 40, 50)

print(t[0])
print(t[-1])
print(t[1:4])

# Traversing
t = (10, 20, 30)

for value in t:
    print(value)


# Immutability
# You cannot modify a tuple.
t = (10, 20, 30)

t[0] = 100   #TypeError


# method
t = (10, 20, 20, 30)

print(t.count(20))   #2
print(t.index(30))   #3



# Tuple operation
a = (1, 2)
b = (3, 4)

print(a + b)  #(1, 2, 3, 4)
print(a * 2)  #(1, 2, 1, 2)
print(2 in a) #True


# tuple unpacking
person = ("Arman", 20, "CSE")

name, age, course = person

print(name)  #arman
print(age)   #20
print(course)  #cse


# swap variable
a = 10
b = 20

a, b = b, a

print(a, b)   #20 10


# nested tuple
data = ((1, 2), (3, 4))

print(data[1][0])   #3


