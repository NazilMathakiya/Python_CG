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
