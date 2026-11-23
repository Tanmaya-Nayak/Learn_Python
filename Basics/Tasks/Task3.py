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
