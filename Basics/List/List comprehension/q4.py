# Print all no. divisible by 5 in the range of 1 - 50
"""
L = []

for i in range(1, 51):
    if i % 5 == 0:
        L.append(i)
    else:
        continue

print(L)
"""

L = [i for i in range(1, 51) if i % 5 == 0]
print(L)
