# Normal Way
squares = []

for i in range(1, 6):
    squares.append(i * i)
print(squares)



# Using comprehensions
squares = [i * i for i in range(1, 6)]
print(squares)


# syntex
# [expression for item in iterable]


# with condition find even number
even = [i for i in range(1, 11) if i % 2 == 0]
print(even)


# if else
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(result)


