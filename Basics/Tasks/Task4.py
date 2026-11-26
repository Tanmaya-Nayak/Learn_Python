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
