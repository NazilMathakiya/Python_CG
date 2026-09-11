# Arithmetic Operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Assignment Operators
x = 10

x += 5
print(x)   # 15

x -= 3
print(x)   # 12

x *= 2
print(x)   # 24

x /= 4
print(x)   # 6.0

# Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

# Logical Operators
# AND
age = 20

print(age >= 18 and age <= 60)

# OR
age = 15

print(age < 18 or age > 60)

# NOT
x = True

print(not x)

# Identity Operators
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)

# Membership Operators
# IN
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)

print("Py" in "Python")

# NOT IN
# print(50 not in numbers)

# Bitwise Operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)

# Complete Example
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)

print("a > b:", a > b)
print("a == b:", a == b)

print("Both conditions:", a > 5 and b < 5)
print("10 in list:", 10 in [5, 10, 15])