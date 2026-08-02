# Find the sum of a three digit no. entered by the user

x = int(input("Enter No. = "))

a = x % 10
x = x // 10

b = x % 10
x = x // 10

c = x % 10
x = x // 10

print(a + b + c)
