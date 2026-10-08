L = [1, 2, 3, 4, 5]
print(L)
del L
# print(L) # error

L1 = [2, 34, 45, 65, 62]

# Indexing
del L1[-1]
print(L1)

# slicing

del L1[0:3]
print(L1)

# Remove

L2 = [12, 123, 45, 22, 34]

L2.remove(22)
print(L2)

L3 = [2, 2, 2, 3]
L3.remove(2)
print(L3)

# pop

L2.pop()  # By default pop(-1) , i.e delete item from last
print(L2)
L2.pop(0)
print(L2)

# Clear

L4 = [1, 23, 53, 66, 45]
L4.clear()
print(L4)

# Operation on list

# Arithmetic Operation

L12 = [1, 2, 3, 4]
L21 = [5, 6, 7, 8]

print(L12 + L21)
print(L12 * 3)

# Membership Operation

L44 = [1, 2, 3, 4, 5]
L23 = [1, 2, 3, 4, [5, 6]]

print(5 in L44)
print(5 in L23)
print([5, 6] in L23)

# Loops

L43 = [1, 2, 3, 4, [5, 6]]

for i in L43:
    print(i)
