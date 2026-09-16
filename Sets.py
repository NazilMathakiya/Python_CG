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



