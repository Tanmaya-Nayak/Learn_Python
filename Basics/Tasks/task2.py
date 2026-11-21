# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# above 20 : 30%

"""
S = float(input("Enter ur salary (in Lakhs):"))

Hra = S * (10 / 100)
Da = S * (5 / 100)
Pf = S * (3 / 100)

if S < 5:
    tax = S * (0 / 100)
elif S >= 5 and S < 10:
    tax = S * (10 / 100)
elif S >= 10 and S < 20:
    tax = S * (20 / 100)
else:
    tax = S * (30 / 100)

annual_salary = S - Hra - Da - Pf - tax
monthly_salary = (annual_salary * 100000) / 12
print("Monthly in-hand salary:", monthly_salary)
"""

# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

"""
A1 = float(input("Enter angle 1: "))
B1 = float(input("Enter angle 2: "))
C1 = float(input("Enter angle 3: "))

Triangle = A1 + B1 + C1

if Triangle == 180:
    print("It is a Triangle")
else:
    print("Not a Triangle")
"""

# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

"""
Cp = float(input("Enter cost price: "))
Sp = float(input("Enter selling price: "))

profit = Sp - Cp

if profit > 0:
    print("Profit")
elif profit < 0:
    print("Loss")
else:
    print("Neither profit nor loss")
"""

# Problem 4: Write a menu-driven program -

# cm to ft
# km to miles
# USD to INR
# exit

"""
print("Menu_Driven")
print("Press 1  for cm to ft")
print("Press 2 for km to miles")
print("Press 3 for USD to INR")
print("Press 4 for exit")

Choice = input("Enter ur choice from 1 to 4: ")

while Choice != 4:
    match Choice:
        case "1":
            cm = float(input("Enter the cm value: "))
            print("The cm to ft conversion is:", cm * 0.0328)
        case "2":
            km = float(input("Enter the km value: "))
            print("The km to miles conversion is:", km * 0.621)
        case "3":
            USD = float(input("Enter the USD value: "))
            print("The USD to INR conversion is:", USD * 92.85)
        case _:
            print("Invalid choice")
print("Exit")
"""

# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.

# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

"""
Fst = 0
Secnd = 1

print(Fst, Secnd, sep=", ", end="")

for i in range(10):
    Sum = Fst + Secnd
    Fst = Secnd
    Secnd = Sum
    print(", ", Sum, sep="", end="")
"""

# Problem 6 - Find the factorial of a given number.

# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

"""
Fac = int(input("factorial of no.: "))
prod = 1

print(Fac, "!", " =", sep="", end="")
while Fac > 0:
    prod = Fac * prod
    print(Fac, end="")
    print("X", end="")
    Fac -= 1
print(": ", prod)
"""


# Problem 7 - Reverse a given integer number.

# Example:

# Input:

# 76542

# Output:

# 24567

"""
n = int(input("Enter no. to reverse: "))

while n > 0:
    t = n % 10
    print(t, end="")
    n = n // 10
"""

# Problem 8: Take a user input as integer N. Find out the sum from 1 to N.
# If any number if divisible by 5, then skip that number.
# And if the sum is greater than 300, don't need to calculate the sum further more.
# Print the final result.
# And don't use for loop to solve this problem.

# Example 1:

# Input:

# 30

# Output:

# 276

"""
N = int(input("Enter N: "))

i = 1
Sum = 0

while i <= N:
    if i % 5 == 0:
        i += 1
        continue
    elif Sum + i <= 300:
        Sum += i
        i += 1
    else:
        break
print(Sum)
"""


# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero.
# Display the sum and average of all the numbers.

"""
I = 1
Sum = 0
NoI = 0
while I != 0:
    I = int(input("I: "))

    if I != 0:
        Sum += I
        NoI += 1

Avg = Sum / NoI
print(Sum)
print(Avg)
"""


# Problem 10: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")
    else:
        continue
"""

# Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a space-separated sequence on a single line.

"""
for i in range(1000, 3001):
    D = i
    Flag = True
    while D > 0:
        S = D % 10
        D = D // 10

        if S % 2 == 0:
            continue
        else:
            Flag = False
            break
    if Flag == False:
        continue
    else:
        print(i, end=",")
"""

# Problem 11: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
#
# The trace of robot movement is shown as the following:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
#
#     The numbers after the direction are steps.
#
#     ! means robot stop there.
#
# Please write a program to compute the distance from current position after a sequence of movement and original point.
#
# If the distance is a float, then just print the nearest integer.
#
# Example:
#
# Input:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
#
# Output:
#
# 2

"""
import math

Up = float(input("UP "))
Dn = float(input("DOWN "))
Lt = float(input("LEFT "))
Rt = float(input("RIGHT "))
print("!")

X1 = 0
Y1 = 0
X2 = abs(Lt - Rt)
Y2 = abs(Up - Dn)

Dist = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)

print(round(Dist))
"""

# Problem 12:Write a program to print whether a given number is a prime number or not

"""
import math

N = int(input("N: "))
for i in range(2, math.isqrt(N) + 1):  # it is an integer square root
    if N % i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")
"""

# Problem 13:Print all the Armstrong numbers in a given range.

# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits.
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

"""
Rng = int(input("Enter range: "))

for i in range(1, Rng):
    CAn = i
    CopyCAn = CAn
    Total = 0
    while CopyCAn > 0:
        S = CopyCAn % 10
        CopyCAn = CopyCAn // 10
        Total += S**3
    if Total == CAn:
        print(Total, end=", ")
    else:
        pass
"""
