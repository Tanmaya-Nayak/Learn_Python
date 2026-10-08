# len/min/max/sorted

L = [1, 54, 22, 75, 67]
print(len(L))
print(min(L))
print(max(L))
print(sorted(L))
print(sorted(L, reverse=True))

# count

L1 = [1, 2, 1, 3, 4, 1]
print(L1.count(1))

# index
print(L1.index(4))
print(L1.index(1))  # 1st occurrence

# sort vs sorted

L2 = [1, 4, 2, 56, 45]
print(sorted(L2))  # not permanent changes the list
print(L2)  # still printing the same original string
L2.sort()  # permanent changes the original list
print(L2)  # original string got changed

# copy

L3 = [1, 22, 43, 55, 65]
print(L3)
print(id(L3))
L4 = L3.copy()
print(L4)
print(id(L4))
