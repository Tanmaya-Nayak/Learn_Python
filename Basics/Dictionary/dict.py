# Empty dictionary
d = {}
print(d)
print(type(d))

# 1D dictionary
d1 = {"name": "sai", "gender": "male"}
print(d1)

# 2D dictionary
s = {
    "name": "sai",
    "sem": 5,
    "subject": {
        "dsa": 66,
        "math": 68,
        "CN": 79,
    },
}

print(s)

# using sequence and dict function
d2 = dict([(1, 1), (2, 2), (3, 3), (4, 4)])
print(d2)

d3 = dict([("name", "sai"), ("age", 21), ("sem", 5)])
print(d3)

# duplicate keys
d4 = {"name": "nitish", "name": "rahul", "name": "sai"}
print(d4)

# mutable item as keys

# d5 = {"name": "sai", [1, 2, 3, 4]: 3} # not allowed
# print(d5)

# Accessing items
my_dict = {"name": "sai", "age": 21}

# []
print(my_dict["age"])

# get
print(my_dict.get("age"))
print("######")
print(s["subject"]["math"])

# Adding key value pair
d5 = {"name": "Abdul", "age": 50}
print(d5)
d5["gender"] = "male"
d5["weight"] = 65
print(d5)

print("#######")

s["subject"]["ds"] = 69
print(s)

# Remove key value pair

# pop
d5.pop("name")
print(d5)

# popitem
d5.popitem()
print(d5)

# del
del d5["age"]
print(d5)

# clear
d5.clear()
print(d5)

# Dictionary operation

# membership
s1 = {
    "name": "sai",
    "sem": 5,
    "collage": "KIIT",
    "subject": {
        "DSA": 87,
        "OS": 77,
        "CN": 98,
    },
}

print("name" in s1)

# iteration
for i in s1:
    print(i, s1[i])

# Dictionary Function
d2 = {"name": "sai", "gender": "male", "age": 21}

# len/min/max/sorted
print(len(d2))
print(sorted(d2))
print(sorted(d2, reverse=True))
print(min(d2))
print(max(d2))

# items/keys/values
print(d2.items())
print(d2.keys())
print(d2.values())

# update
d3 = {1: 2, 3: 4, 4: 5}
d4 = {4: 7, 6: 8}

d3.update(d4)
print(d3)
