student = {
    "name": "Nazil",
    "age": 20,
    "course": "CSE"
}

print(student["name"])
print(student["age"])

# Add / Update
student["marks"] = 85
student["age"] = 21
print(student)


# remove
student.pop("age")

# Remove the last item:
student.popitem()

# Remove everything:
student.clear()


student = {"name": "Arman", "age": 20}

print("name" in student)   #true
print("marks" in student)  #false


# traversing
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)


# imp method
student = {"name": "Arman", "age": 20}

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))

student.update({"marks": 90})
print(student)

student.pop("age")
print(student)


# nested dict
students = {
    "student1": {
        "name": "Arman",
        "marks": 85
    },
    "student2": {
        "name": "Rahul",
        "marks": 90
    }
}

print(students["student1"]["marks"])


# count character
text = "banana"

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)   #{'b': 1, 'a': 3, 'n': 2}


# dict with list
data = {
    "fruits": ["apple", "banana"],
    "numbers": [1, 2, 3]
}

print(data["fruits"][0])  #apple


