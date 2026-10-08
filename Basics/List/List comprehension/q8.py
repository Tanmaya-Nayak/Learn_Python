# cartesian products -> List comprehension on 2 lists together

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print([i * j for i in L1 for j in L2])
