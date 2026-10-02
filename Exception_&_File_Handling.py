# try-except
try:
    num= int(input("enter a number::"))
    print(num)

except ValueError:
    print("enter a valid data!!")



# else and finally
try:
    num= int(input("enter a number::"))
except ValueError:
    print("enter valid value!")
else:
    print(num)
finally:
    print("Thank You!!")



# raise (manually create exception)
age = -5
if age < 0:
    raise ValueError("age cannot be negative!")



# File Handling
# Read file
with open("data.txt", "r") as file:
    content = file.read()

print(content)    #with automatically closes the file.



# write
with open("data.txt", "w") as file:
    file.write("Hello Nazil")    #w overwrites existing content.



# appending
with open("data.txt", "a") as file:
    file.write("\nPython")      #a adds content to the end.