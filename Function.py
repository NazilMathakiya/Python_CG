def greet():
    print("Hello Nazil")

greet()   #Hello Nazil


# Parameters and Arguments
def greet(name):
    print("Hello", name)

greet("Nazil")    #name → parameter ,, "Nazil" → argument


# return
def add(a, b):
    return a + b

result = add(10, 20)

print(result)  #30


# default parameter
def greet(name="Nazil"):
    print("Hello", name)

greet()
greet("Arman")


# keyword argument
def student(name, age):
    print(name, age)

student(age=20, name="Nazil")


# *args
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40))



# **kwargs
def student(**data):
    print(data)

student(name="Nazil", age=20, course="CSE")





