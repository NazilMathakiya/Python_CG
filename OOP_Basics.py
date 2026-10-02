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



