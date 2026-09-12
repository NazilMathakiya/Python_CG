# String
name = "Arman"
city = 'Rajkot'

# indexing
text = "Python"

print(text[0])   # P
print(text[2])   # t
print(text[-1])  # n

# Slicing
# string[start:stop:step]
# stop is not included.
text = "Python"

print(text[0:3])   # Pyt
print(text[2:])    # thon
print(text[:4])    # Pyth
print(text[::2])   # Pto
print(text[::-1])  # nohtyP

# Traversing a String
text = "Hello"

for ch in text:
    print(ch)