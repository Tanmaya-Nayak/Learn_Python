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

"""
S = input("S: ")
Len = len(S)

print(S[0].upper(), end="")
for i in range(Len):
    if S[i] == " " and i + 1 < Len:
        print(S[i + 1].upper(), end="")
    else:
        pass
"""

# Problem 12: Append second string in the middle of first string
#
# Input:
#
# campusx
# data
#
# Output:
#
# camdatapusx

"""
S = input("S: ")
Len = len(S)
S1 = input("S1: ")


if Len % 2 == 0:
    Mid = int(Len / 2)
else:
    Mid = int((Len + 1) / 2)

K = Mid

for i in range(Mid):
    if i == Mid:
        print(S1, end="")
    else:
        print(S[i], end="")


while K < Len:
    print(S[K], end="")
    K += 1
"""

"""
S = input("S: ")
Len = len(S)
S1 = input("S1: ")

Mid = Len // 2

for i in range(Mid):
    print(S[i], end="")

print(S1, end="")

K = Mid
while K < Len:
    print(S[K], end="")
    K += 1
"""

# Problem 13:Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
#
# Given:
#
# str1 = PyNaTive
#
# Expected Output:
#
# yaivePNT

"""
Str1 = input("str1: ")
Len = len(Str1)

for i in range(Len):
    if Str1[i] >= "a" and Str1[i]<= "z":
        print(Str1[i], end="")
for i in range(Len):
    if Str1[i] >= "A" and Str1[i] <= "Z":
        print(Str1[i], end="")
"""


# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string,
# ignoring all other characters.
#
# Input:
#
# hel123O4every093
#
# Output:
#
# Sum: 22
# Avg: 2.75

"""
Alpnum = input("Alpnum: ")
Len = len(Alpnum)
Sum = 0
Count = 0

for i in range(Len):
    if Alpnum[i] >= "a" and Alpnum[i] <= "z" or Alpnum[i] >= "A" and Alpnum[i] <= "Z":
        pass
    else:
        Count += 1
        Sum += int(Alpnum[i])

Avg = Sum / Count
print(Sum)
print(Avg)
"""

"""
Alpnum = input("Alpnum: ")
Len = len(Alpnum)

Sum = 0
Count = 0

for i in range(Len):
    if Alpnum[i].isdigit():
        Count += 1
        Sum += int(Alpnum[i])

Avg = Sum / Count

print("Sum:", Sum)
print("Avg:", Avg)
"""

# Problem 15: Removal of all characters from a string except integers
#
# Given:
#
# str1 = 'I am 25 years and 10 months old'
#
# Expected Output:
#
# 2510

"""
Str1 = input("str1: ")
Len = len(Str1)

for i in range(Len):
    if Str1[i].isalpha() or Str1[i] == " ":
        pass
    else:
        print(Str1[i], end="")
"""


# Problem 16: Check whether the string is Symmetrical.
#
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.
#
# Example 1:
#
# Input
#
# khokho
#
# Output
#
# The entered string is symmetrical

"""
S = input("S: ")
Len = len(S)
Mid = Len // 2

if Len % 2 != 0:
    print("The entered string is NOT symmetrical")
elif S[0:Mid] == S[Mid:Len]:
    print("The entered string is symmetrical")
else:
    print("The entered string is NOT symmetrical")
"""

#### Problem 17: Reverse words in a given String ####
#
# Statement: We are given a string and we need to reverse words of a given string.
#
# Example 1:
#
# Input:
#
# geeks quiz practice code
#
# Output:
#
# code practice quiz geeks
#
# Example 2:
#
# Input:
#
# my name is laxmi
#
# Output:
#
# laxmi is name my

"""
S = input("S: ")
Len = -len(S)

Rbound = None

for i in range(-1, Len - 1, -1):
    if S[i] == " ":
        print(S[i + 1 : Rbound], end=" ")
        Rbound = i

print(S[:Rbound])
"""

# Problem 18: Find uncommon words from two Strings.
#
# Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words.
# A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence.
# Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.
#
# Example 1:
#
# Input:
#
# A = "apple banana mango"
# B = "banana fruits mango"
#
# Output:
#
# ['apple', 'fruits']

"""
A = input("A: ")
B = input("B: ")

A_words = A.split()
B_words = B.split()

Uncommon = []

for word in A_words:
    if word not in B_words and A_words.count(word) == 1:
        Uncommon.append(word)

for word in B_words:
    if word not in A_words and B_words.count(word) == 1:
        Uncommon.append(word)

print(Uncommon)
"""

# Problem 19: Word location in String.
#
# Statement: Find a location of a word in a given sentence.
#
# Example 1:
#
# Input:
#
# Sentence: We can learn data science through campusx mentorship program.
#
# word: campusx
#
# Output:
#
# Location of the word is 7.
#
# Note- Don't use index/find functions

"""
Sentence = input("Sentence: ")
Word = input("Word: ")

Words = Sentence.split()

Count = 1

for i in range(len(Words)):
    if Words[i] == Word:
        print("Location of the word is", Count)
        break
    Count += 1
"""
# Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.

S = input("S: ")

Result = ""

for char in S:
    if char not in Result:
        Result += char

print(Result)
