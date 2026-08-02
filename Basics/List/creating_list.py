# Empty list
print([])

# 1D list -> Homogenous list , contains only single type of elements
print([1, 2, 3, 4, 5, 6])

# 2D list
print([1, 2, 3, 4, [1, 2, 3, 4]])

# Heterogenous
print([True, 2.34, "sdssd", 1 + 5j])

# Using type conversion
print(list("hello"))

# Indexing

L = [1, 2, 3, 5, 6]

print(L[0])
print(L[1])
print(L[-1])
print(L[-2])

L1 = [1, 2, 3, [4, 5]]
print(L1[-1])
print(L1[-1][-2])
print(L1[3][1])

# slicing

L2 = [1, 2, 3, 4, 5]
print(L2[0:3])  # 1,2,3
print(L2[-3:])  # 3,4,5
print(L2[0::2])  # 1,3,5
print(L2[-5:-2:2])  # 1,3
print(L2[::-1])  # reverse list

# Adding item to list

# append

s = [1, 2, 3, 4, 5]
s.append(6)
print(s)

# extend
L = [1, 2, 3, 4, 5]
L.extend([6, 7, 8])
print(L)

L1 = [1, 2, 3, 4, 5]
L1.append([6, 7, 8])
print(L1)
L1.extend("delhi")
print(L1)

# insert at desired place in list

L2 = [1, 2, 3, 4, 5]
L2.insert(2, 67)
print(L2)

# Edit items in a list

L3 = [1, 2, 3, 4, 5]
L3[-1] = 67
print(L3)

L3[1:4] = [122, 324, 545]
print(L3)
