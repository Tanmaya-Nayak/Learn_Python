# Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

"""
for i in range(5):
    for j in range(5, 0, -1):
        if j - i > 0:
            print(j - i, end=" ")
        else:
            pass
    print()
"""

# Problem 2: Print the following pattern.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

"""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
"""

# Problem 3:Write a program to print the following pattern
#
#     *
#   * * *
# * * * * *

"""
for i in range(1, 4):
    for j in range(2 * (3 - i)):
        print(end=" ")
    for k in range((2 * i) - 1):
        print("*", end=" ")
    print()
"""

# Problem 4:Write a program to print the following pattern

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

"""
for i in range(5):
    for j in range(i + 1, 0, -1):
        print(j, end=" ")
    print()
"""

# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:

# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

"""
N = int(input("N: "))
X = int(input("X: "))
Sum = 1

for i in range(2, N + 1):
    S = X**i / i
    Sum += S

print(Sum)
"""

# Problem 6: The natural logarithm can be approximated by the following series.
# temp.jpg
# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.

"""
X = float(input("X: "))
Sum = (X - 1) / X

for i in range(2, 8):
    S = 0.5 * ((X - 1) / X) ** i
    Sum += S

print(Sum)
"""

# Problem 7 - Find the sum of the series upto n terms.
#
# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690.
# Take the user input and then calculate. And the output style should match which is given in the example.
#
# Example 1:
#
# Input:
#
# 5
#
# Output:
#
# 2+22+222+2222+22222
# Sum of above series is: 24690

"""
N = int(input("N: "))
Sum = 2

print(Sum, end="")
for i in range(1, N):
    S = 1
    j = i
    while j > 0:
        S += 10 ** (j)
        j -= 1
    S = 2 * S
    print("+", S, sep="", end="")
    Sum += S
print()
print("Sum of above series is:", Sum)
"""


### Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4###
#
# Output:
#
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on

"""
for A in range(1, 5):
    for B in range(1, 5):
        for C in range(1, 5):
            for D in range(1, 5):
                if A != B and A != C and A != D and B != C and B != D and C != D:
                    print(A, B, C, D)
"""

# Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number

"""
N = int(input("N: "))

S = N
C = 0
Ans = 0
while S > 0:
    B = S % 2
    S = S // 2
    Ans += B * (10**C)
    C += 1
print(Ans)
"""

# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

"""
N1 = int(input("N1: "))
N2 = int(input("N2: "))

A = N1
B = N2

LCM = 1
HCF = 1
i = 2

while i <= min(A, B):
    if A % i == 0 and B % i == 0:
        A //= i
        B //= i
        LCM *= i
        HCF *= i
    else:
        i += 1

LCM = LCM * A * B

print("LCM:", LCM)
print("HCF:", HCF)
"""

# Problem 11: Create Short Form from initial character
#
# Given a string create short form of the string from Initial character. Short form should be capitalised.
#
# Example:
#
# Input:
#
# Data science mentorship program
#
# Output:
#
# DSMP
