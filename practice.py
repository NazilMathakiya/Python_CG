# print("Hello, World!")
# print("I am learning Python.")
# print("Python will help me learn DSA.")
##

# name = "Arman"
# age = 20

# print(name)
# print(age)

##

# a = 10
# b = 20

# print(a + b)
##

# import math;
# print(math.sqrt(49));
##

# name =  "Nazil";
# age = 18;
# print(name);
# print(age);
##

# name = "Arman"
# age = 20
# marks = 85

# print("Name:", name)
# print("Age:", age)
# print("Marks:", marks)
##

# print("Arman", 20, 85, sep=" | ")

###




# test question:
# missing number
num = [1, 2, 3, 5]

for i in range(1, 6):
    if i not in num:
        print(i)


# second largest
num = [10, 5, 20, 8, 15]

largest = num[0]
second = num[0]

for i in num:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)

# 