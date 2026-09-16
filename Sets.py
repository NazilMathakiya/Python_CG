# A set is an unordered collection of unique elements.

numbers = {10, 20, 30, 20}
print(numbers)  #{10, 20, 30}


# creating a set
s = {1, 2, 3}

# empty set
s = set()
# {} creates an empty dictionary, not a set.


# add element
s = {1, 2, 3}

s.add(4)

print(s)  


# update
s.update([5, 6, 7])

print(s)


# remove element
# remove()
s = {1, 2, 3}

s.remove(2)  #give error if element does not exist keyerror


# discard()
s.discard(10)  #no error


# pop()
s.pop()


# clear()
s.clear()


# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union
print(a | b)   #{1, 2, 3, 4, 5, 6}
a.union(b)


# Intersection
print(a & b)  #{3, 4}
a.intersection(b)


# Difference
print(a - b)    #{1, 2}


# Symmetric Difference
print(a ^ b)   #{1, 2, 5, 6}


# membership
numbers = {10, 20, 30}

print(20 in numbers)   #true
print(50 in numbers)   #false


# Set Comparison
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
print(b.issuperset(a))


a.isdisjoint(b)
# Checks whether two sets have no common elements.


# Traversing
numbers = {10, 20, 30}

for num in numbers:
    print(num)


# Set Comprehension
squares = {x * x for x in range(5)}

print(squares)   #{0, 1, 4, 9, 16}
