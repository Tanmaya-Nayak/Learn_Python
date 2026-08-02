x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

if x < y and x < z:
    print(x)
elif y < x and y < z:
    print(y)
else:
    print(z)
