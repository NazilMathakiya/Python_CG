# For Loop
for i in range(5):
    print(i)


# Range
# range(start, stop, step)
for i in range(1, 6):
    print(i)

# Step
for i in range(2, 11, 2):
    print(i)

# Nested-Loop
for i in range(3):
    for j in range(2):
        print(i, j)

# Break
# stop the loop immediately
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Continue
# Skips the current iteration and moves to the next one.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Pass
# Does nothing. Used as a placeholder.
for i in range(5):
    pass

# else with loop
# The else executes when the loop finishes normally (without break).
for i in range(3):
    print(i)
else:
    print("Loop completed")

# If break happens, else does not execute:
for i in range(5):
    if i == 2:
        break
else:
    print("Completed")\


# example- Even Number
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

        