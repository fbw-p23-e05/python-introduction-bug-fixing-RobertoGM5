x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or x == z:
    sum = 0
else:
    sum = x + y + z
print("Calculated sum is ", sum)