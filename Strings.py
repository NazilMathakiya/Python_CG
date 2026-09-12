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

# string operators
a = "Hello"
b = "World"

print(a + " " + b)  # concatenation
print(a * 3)        # repetition
print("H" in a)    # membership

#  String Methods
text = "  Hello Python  "

print(text.upper())       # HELLO PYTHON
print(text.lower())       # hello python
print(text.strip())       # removes spaces
print(text.replace("Python", "World"))
print(text.split())       # converts to list

# other methods
text = "hello python"

text.startswith("hello")  #True
text.endswith("python")  #True
text.find("python")  #6
text.count("o")   #2

# Len
text = "Python"

print(len(text))