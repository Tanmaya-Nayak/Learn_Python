# Q1 :- Print the given strings as per stated format.

# Given strings:

# "Data" "Science" "Mentorship" "Program"
# "By" "CampusX"

# Output:

# Data-Science-Mentorship-Program-started-By-CampusX

# Concept- [Seperator and End]

"""
a = input("Enter 1st string: ")
b = input("Enter 2nd string: ")
c = input("Enter 3rd string: ")

print(a, b, c, sep="-")
"""

# Q2:- Write a program that will convert celsius value to fahrenheit.

"""
c = float(input("Enter the value of c: "))
f = c * (9 / 5) + 32
print(f)
"""

# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

"""
a = int(input("enter a = "))
b = int(input("enter b = "))
temp = a
a = b
b = temp
print("a =", a, "b =", b)
"""

# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

"""
import math

x1 = int(input("Enter x1 = "))
y1 = int(input("Enter y1 = "))
x2 = int(input("Enter x2 = "))
y2 = int(input("Enter y2 = "))

e = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(e)
"""

# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""
p = int(input("Enter principle: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time period: "))
t = t / 12
SI = (p * t * r) / 100
print(SI)
"""

# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2

"""
H = int(input("Enter No. of heads: "))
L = int(input("Enter No. of Legs: "))
Dogs = 0
Chickens = 0
while L > 0:
    if L % 4 == 0:
        Dogs += 1
        L -= 4
    else:
        Chickens += 1
        L -= 2

print("Dogs ->", Dogs, "Chickens ->", Chickens)
"""

# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

"""
n = int(input("Enter n: "))
sum = (n * (n + 1) * (2 * n + 1)) / 6
print("Sum of", n, "numbers are:", sum)
"""

# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

"""
a = float(input("Enter 1st input: "))
b = float(input("Enter 2nd input: "))
d = b - a
n = int(input("Enter the nth term u want to find: "))

Result = a + (n - 1) * d
print(n, "th term: ", Result, sep="")
"""

# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

"""
n1 = int(input("Enter numerator of 1st fraction: "))
d1 = int(input("Enter denominator of the 1st fraction: "))
n2 = int(input("Enter numerator of the 2nd fraction: "))
d2 = int(input("Enter denominator of the 2nd fraction: "))

F_n = (d2 * n1) + (d1 * n2)
F_d = d1 * d2

result = F_n / F_d
print("sum of 2 fn. :", result)
"""

# q10:- given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? assume all the inputs are provided by the user.

# input:
# dimensions of the milk tank
# h = 20cm, l = 20cm, b = 20cm

# dimensions of the glass
# h = 3cm, r = 1cm

length = float(input("enter the length of milk tank: "))
breadth = float(input("enter the breadth of milk tank: "))
height1 = float(input("enter the height of milk tank: "))

radius = float(input("enter radius of glass: "))
height2 = float(input("enter height of glass: "))

area_cuboid = length * breadth * height1
area_cylinder = 3.14 * radius**2 * height2

result = area_cuboid // area_cylinder

print("total glass required: ", result)
