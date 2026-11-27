# Problem 1: Combine two lists index-wise(columns wise)
#
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#
# Given List:
#
# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
#
# Output:
#
# [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]

"""
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
list3 = []
L = []
Len1 = len(list1)
Len2 = len(list2)
Mxlen = max(Len1, Len2)
Milen = min(Len1, Len2)
for i in range(Mxlen):
    if i < Milen:
        L.extend([list1[i], list2[i]])
        CL = L.copy()
        list3.append(CL)
        L.clear()
    elif Len1 < Len2:
        list3.extend([list2[i]])
    else:
        list3.extend([list1[i]])
print(list3)
"""

"""
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

Len1 = len(list1)
Len2 = len(list2)
Milen = min(Len1, Len2)

list3 = [[list1[i], list2[i]] for i in range(Milen)]

if Len1 < Len2:
    list3 += [list2[i] for i in range(Milen, Len2)]
else:
    list3 += [list1[i] for i in range(Milen, Len1)]

print(list3)
"""

# Problem 2: Add new item to list after a specified item
#
# Write a program to add item 7000 after 6000 in the following Python List
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# Output:
#
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
"""

# Problem 3: Update no of items available
#
# Suppose you are given a list of candy and another list of same size representing no of items of respective candy.
#
# i.e -
#
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]
#
# Write a program to show no. of items of each candy type.
#
# Output:
#
# Jelly Belly-10
# Kit Kat-20
# Double Bubble-34
# Milky Way-74
# Three Musketeers-32

"""
candy_list = [
    "Jelly Belly",
    "Kit Kat",
    "Double Bubble",
    "Milky Way",
    "Three Musketeers",
]
no_of_items = [10, 20, 34, 74, 32]
Len = len(no_of_items)

Output = [candy_list[i] + "-" + str(no_of_items[i]) for i in range(Len)]

for i in Output:
    print(i)
"""

# Problem 4: Running Sum on list
#
# Write a program to print a list after performing running sum on it.
#
# i.e:
#
# Input:
#
# list1 = [1,2,3,4,5,6]
#
# Output:
#
# [1,3,6,10,15,21]

"""
list1 = [1, 2, 3, 4, 5, 6]
Sum = 0
Flist = []

for i in range(len(list1)):
    Sum += list1[i]
    Flist.append(Sum)
print(Flist)
"""

# Problem 5: You are given a list of integers.
# You are asked to make a list by running through elements of the list by adding all elements greater and itself.
#
# i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].
#
# For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.
#
# For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20
#
# like wise for all other elememts.
#
# [2,4,6,10,1]-->[22,20,16,10,23]

"""
L = [2, 4, 6, 10, 1]
Len = len(L)
Flist = []
for i in range(Len):
    Sum = 0
    for j in range(Len):
        if L[i] <= L[j]:
            Sum += L[j]
        else:
            continue
    Flist.append(Sum)
print(L, "->", Flist)
"""

"""
L = [2, 4, 6, 10, 1]
Output = [sum(j for j in L if j >= i) for i in L]
print(Output)
"""

# Problem 6: Find list of common unique items from two list. and show in increasing order
#
# Input
#
# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
#
# Output:
#
# [34, 67, 89]

"""
num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]
num3 = []
Len1 = len(num1)
Len2 = len(num2)
MinLen = min(Len1, Len2)
MaxLen = max(Len1, Len2)
for i in range(MinLen):
    for j in range(MaxLen):
        if num1[i] == num2[j]:
            num3.append(num1[i])
num3.sort()
print(num3)
"""
"""
num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]

num3 = []

for i in num1:
    for j in num2:
        if i == j and i not in num3:
            num3.append(i)

num3.sort()
print(num3)
"""

# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it.
# If in any string there is no numeric character take it's product value as 1.
#
# Input:
#
# ['1ac21', '23fg', '456', '098d','1','kls']
#
# Output:
#
# ['456', '23fg', '1ac21', '1', 'kls', '098d']

"""
Anum = ["1ac21", "23fg", "456", "098d", "1", "kls"]
Num = []
for i in Anum:
    Prod = 1
    if i.isalpha():
        Num.append(1)
    elif i.isdigit():
        Num.append(int(i))

    elif i.isalnum():
        for j in range(len(i)):
            if i[j].isdigit():
                Prod *= int(i[j])
        Num.append(Prod)
    else:
        continue

Tempo = [[Anum[i], Num[i]] for i in range(len(Anum))]

for i in range(len(Tempo)):
    for j in range(i + 1, len(Tempo)):
        if Tempo[i][1] < Tempo[j][1]:
            Tempo[i], Tempo[j] = Tempo[j], Tempo[i]

Output = [i[0] for i in Tempo]
print(Output)
"""

# Problem 8: Split String of list on K character.
#
# Example :
#
# Input:
#
# ['CampusX is a channel', 'for data-science', 'aspirants.']
#
# Output:
#
# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

"""
I = ["CampusX is a channel", "for data-science", "aspirants."]
Fa = []
for i in I:
    Slt = i.split()
    for j in range(len(Slt)):
        Fa.append(Slt[j])
print(Fa)
"""

# Problem 9: Convert Character Matrix to single String using string comprehension.
#
# Example 1:
#
# Input:
#
# [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
#
# Output:
#
# campux is best channel

"""
I = [
    ["c", "a", "m", "p", "u", "x"],
    ["i", "s"],
    ["b", "e", "s", "t"],
    ["c", "h", "a", "n", "n", "e", "l"],
]
O = " ".join(["".join([I[j][i] for i in range(len(I[j]))]) for j in range(len(I))])
print(O)
"""
"""
I = [
    ["c", "a", "m", "p", "u", "x"],
    ["i", "s"],
    ["b", "e", "s", "t"],
    ["c", "h", "a", "n", "n", "e", "l"],
]

O = " ".join(["".join(word) for word in I])
print(O)
"""

# Problem 10: Add Space between Potential Words.
#
# Example:
#
# Input:
#
# ['campusxIs', 'bestFor', 'dataScientist']
#
# Output:
#
# ['campusx Is', 'best For', 'data Scientist']

"""
I = ["campusxIs", "bestFor", "dataScientist"]
J = []

for i in I:
    New = ""
    for j in range(len(i)):
        if i[j] >= "a" and i[j] <= "z":
            New += i[j]
        else:
            New += " "
            New += i[j]
    J.append(New)
print(J)
"""

# Problem 11: Write a program that can perform union operation on 2 lists
#
# Example:
#
# Input:
#
# [1,2,3,4,5,1]
# [2,3,5,7,8]
#
# Output:
#
# [1,2,3,4,5,7,8]

"""
L1 = [1, 2, 3, 4, 5, 1]
L2 = [2, 3, 5, 7, 8]
L3 = []

for i in L1:
    for j in L2:
        if (i != j and i not in L3) or (i == j and i not in L3):
            L3.append(i)
        elif j not in L3:
            L3.append(j)
    if i not in L3:
        L3.append(i)
L3.sort()
print(L3)
"""
"""
L1 = [1, 2, 3, 4, 5, 1]
L2 = [2, 3, 5, 7, 8]
L3 = []

for i in L1:
    if i not in L3:
        L3.append(i)


for i in L2:
    if i not in L3:
        L3.append(i)

print(L3)
"""

# Problem 12: Write a program that can find the max number of each row of a matrix
#
# Example:
#
# Input:
#
# [[1,2,3],[4,5,6],[7,8,9]]
#
# Output:
#
# [3,6,9]

"""
# I = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
I = [[9, 3, 5], [4, 2, 1], [-5, -2, -9]]
Mxelm = []

for i in I:
    Max = i[0]
    for j in range(1, len(i)):
        if Max < i[j]:
            Max = i[j]
    Mxelm.append(Max)
print(Mxelm)
"""

# Problem 13: Write a list comprehension to print the following matrix
#
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

"""
Output = [[i + 3 * j for i in range(3)] for j in range(3)]
print(Output)
"""

# Problem 14: Write a list comprehension that can transpose a given matrix
#
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
#
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

"""
Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output = [[Matrix[i][j] for i in range(len(Matrix))] for j in range(len(Matrix))]

for i in Output:
    print(i)
"""

# Problem 15: Write a list comprehension that can flatten a nested list
#
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
#
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output = [i[j] for i in Matrix for j in range(len(i))]
#Output = [j for i in Matrix for j in i]
print(Output)
"""
