x = int(input("Enter till the sequence will run: "))

y = 1

for i in range(1, x + 1):
    print(i, "/", y, end=" + ")
    y *= i + 1

if x == 0:
    print(1)
