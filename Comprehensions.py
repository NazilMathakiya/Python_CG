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
print(result)    #['Odd', 'Even', 'Odd', 'Even', 'Odd']


# set comprehension
squares = {i * i for i in range(1, 6)}
print(squares)    #{1, 4, 9, 16, 25}


# dictionary'
squares = {i: i * i for i in range(1, 6)}
print(squares)
