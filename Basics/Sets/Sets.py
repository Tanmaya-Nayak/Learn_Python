# empty
"""
s = {}
print(s) # {}
print(type(s)) # <class 'dict'>
"""

s = set()
print(s)
print(type(s))

# 1D and 2D

s1 = {1, 2, 3, 4}
print(s1)

"""
s2 = {1,2,3,4,{5,6}} # u cann't have mutable data type inside a set 
print(s2)
"""

s2 = {1, "hello", 4.5, True}
print(
    s2
)  # {1,4.5,'hello'} # no true bcz , their is not duplicate in sets and ture is 1 too.

# using type conversion

s3 = set([1, 2, 3, 4])
print(s3)

# Duplicates not allowed
s4 = {1, 3, 2, 4, 4, 3, 6, 5, 6, 5}
print(s4)

# sets can't have mutable items
"""
s5 = {1,2,[3,4]} # as we know , we cannt able to use mutable data type inside sets 
print(s5)
"""

# Accesing items
"""
s5 = {1, 2, 3, 4, 5, 6}
print(s5[0]) #not allowed
print(s5[-1])
print(s5[0:3])
"""

# Editing items
"""
s5 = {1,2,3}
s5[0] = 20 #Not allowed
print(s5)
"""

# Updates
s5 = {1, 2, 3}

# add
s5.add(4)
print(s5)

# updates
s5.update([5, 6, 7])
print(s5)

# Deleting items
"""
s6 = {1, 2, 3, 4}
del s6   # it will work
del s6[0] # it will not work , as indexing not working
print(s6)
"""

# discard
s5.discard(7)
print(s5)

s5.discard(34)  # No error

# remove
s5.remove(6)
print(s5)

"""
s5.remove(34)
print(s5)  # error
"""

# pop
print(s5.pop())

# clear
s5.clear()
print(s5)

# Set operation

s6 = {1, 2, 3, 4, 5}
s7 = {4, 5, 6, 7, 8}
# union(|)
print(s6 | s7)

# Intersection (&)
print(s6 & s7)

# Difference (-)
print(s6 - s7)
print(s7 - s6)

# Symmetric Difference
print(s6 ^ s7)

# Membership operator
print(1 in s6)
print(1 not in s6)

# Iterator
for i in s6:
    print(i, end=" ")
print()

# Set Functions

S = {2, 4, 3, 5, 67, 87, 55}
# len/sum/min/max/sorted
print(len(S))
print(sum(S))
print(min(S))
print(max(S))
print(sorted(S))  # output is always in list
print(sorted(S, reverse=True))

# union/update
S1 = {1, 2, 3, 4, 5}
S2 = {4, 5, 6, 7, 8}

"""
print(S1.union(S2))
print(S1)
S1.update(S2)
print(S1)  # will get changed, will get all elements of s2 in s1, permanently
"""

# Intersection/Intersection_update

print(S1.intersection(S2))
print(S1)

"""
S1.intersection_update(S2)
print(S1)
"""

# Difference/Difference_update

print(S1.difference(S2))

"""
S1.difference_update(S2)
print(S1)
"""

# Symmetric_difference/Symmetric_Difference_update
print(S1.symmetric_difference(S2))

"""
S1.Symmetric_Difference_update(S2)
print(S1)
"""

# isdisjoint/issubset/issuperset
s3 = {1, 2, 3, 4, 5}
s4 = {2, 3, 4}
print(S1.isdisjoint(S2))
print(s4.issubset(s3))
print(s3.issuperset(s4))

# copy

S3 = {1, 2, 3, 4}
S4 = S3.copy()
print(S4)

# Frozenset
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(fs1 | fs2)

fs = frozenset([1, 2, frozenset([3, 4])])
print(fs)

# Set comprehension

print({i for i in range(1, 11)})
