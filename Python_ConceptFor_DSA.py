# reference
a = [1, 2, 3]
b = a
b.append(4)
print(a)


# copying
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)



# deep copy
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99

print(a)
print(b)



# Unpacking
a, b, c = [10, 20, 30]

print(a)
print(b)
print(c)



# * Unpacking
numbers = [1, 2, 3]
print(*numbers)   # 1 2 3


a, *rest = [1, 2, 3, 4]
print(a)
print(rest)   #1, [2, 3, 4]



# ** Dictionary Unpacking
a = {"name": "Nazil"}
b = {"age": 20}

result = {**a, **b}
print(result)      #{'name': 'Nazil', 'age': 20}







