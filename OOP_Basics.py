# class and object
class Student:
    def greet(self):
        print("Hello Nazil")

student = Student()
student.greet()


# Constructor __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Nazil", 20)

print(student.name)
print(student.age)



# Instance Methods
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()

print(calc.add(10, 20))



# class variable
class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

a = Student("Nazil")
b = Student("Rahul")

print(a.college)
print(b.college)



# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()



# Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()