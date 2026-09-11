# IF
age = 20

if age >= 18:
    print("Adult")

# IF-ELSE
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

# IF-ELIF-ELSE
marks = 50

if marks>80:
    print("Excellent")
elif marks>70:
    print("Very good")
elif marks>60:
    print("good")
elif marks>40:
    print("Average")
else:
    print("Fail!!")

# Nested-If
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

# Logical Conditions
# AND
age = 25

if age >= 18 and age <= 60:
    print("Eligible")

# OR
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

# NOT
is_raining = False

if not is_raining:
    print("Go outside")

# Complete Example
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# odd even
num = 4
if num%2==0:
    print("even")
else:
    print("odd")