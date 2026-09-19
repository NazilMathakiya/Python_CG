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