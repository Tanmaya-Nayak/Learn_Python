# empty
t1 = ()
print(t1)

# create a tuple with a single item
t2 = ("hello",)
print(t2)
print(type(t2))

# homo
t3 = (1, 2, 3, 4, 5)
print(t3)

# hetro
t4 = (1, 2.3, True, [1, 2, 3])
print(t4)

# 2D tuple
t5 = (1, 2, 3, (4, 5))
print(t5)

# using type conversion
t6 = tuple("hello")
print(t6)

# Access item
t7 = (1, 2, 3, 4, 5)
print(t7[0:4])
print(t7[-3:-1])
print(t7[::-1])  # reverse
# t5 = (1,2,3,(4,5))
print(t5[-1][0])

# Edit tuple

# t3[0] = 100; #u cannt able to make changes in tuple , bcz tuple is immutable;

# del tuple

t8 = (1, 2, 3, 4, 5)
print(t8)
del t3
# print(t3) # it will del the whole tuple

print(t5)
# del t5[-1] # will not work

# operator in tuple

t9 = (1, 2, 3, 4, 5)
t11 = (6, 7, 8)
print(t9 + t11)  # (1,2,3,4,5,6,7,8)
print(t9 * 2)  # (1,2,3,4,5,1,2,3,4,5)

# membership
print(1 in t9)

# iterator
for i in t11:
    print(i, sep="", end=" ")
print()
# Tuple function

# len/min/max/sorted/sum
t22 = (1, 2, 3)
print(len(t22))
print(sum(t22))
print(min(t22))
print(max(t22))
print(sorted(t22))
print(sorted(t22, reverse=True))

# count
print(t22.count(1))

# index
print(t22.index(2))

# Special Syntax

a, b, c = (1, 2, 3)
print(a, b, c)

# Swap
c = 1
d = 4
c, d = d, c
print(c, d)

g, h, *other = (1, 2, 3, 5)
print(g, h)
print(other)

# zip
k = (1, 2, 3, 4)
s = (5, 6, 7, 8)

print(zip(k, s))
print(list(zip(k, s)))
print(tuple(zip(k, s)))
