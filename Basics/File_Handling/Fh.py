######File Handling######

# If the file is not present
f = open("sample.txt", "w")
f.write("Hello World")
f.close()
# As the file is closed hence no further write operation will work
# f.write("hello")

# write multiple strings
f = open("sample1.txt", "w")
f.write("hello world\n")
f.write("how are you ?")
f.close()

# if the file is already present
f = open("sample.txt", "w")
f.write("mew the bili")
f.close()

# introduction to append
f = open("sample1.txt", "a")
f.write("\ni am fine")
f.close()

# writelines
l = ["hello\n", "hi\n", "how are you\n", "i am fine"]
f = open("sample.txt", "w")
f.writelines(l)
f.close()

# read from file
f = open("sample.txt", "r")
s = f.read()
# print(s)
f.close()

# to read line by line
f = open("sample.txt", "r")
# print(f.readline(), end="")
# print(f.readline(), end="")
f.close()

# read entire file with readline
"""
f = open("sample.txt", "r")

while True:
    data = f.readline()

    if data == "":
        break
    else:
        print(data, end="")
f.close()
"""

# with

with open("sample.txt", "w") as f:
    f.write("its me sai")

# read by using with

with open("sample.txt", "r") as f:
    print(f.read())

"""
# to load a big file in a memory
big_L = ["hello world" for i in range(1000)]

with open("big.txt", "w") as f:
    f.writelines(big_L)

with open("big.txt", "r") as f:
    chunk_size = 10

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end="***")
        f.read(chunk_size)
"""

# seek and tell function
with open("sample.txt", "r") as f:
    f.seek(15)
    print(f.read(10))
    print(f.tell())

    print(f.read(10))
    print(f.tell())

# seek during write
with open("sample.txt", "w") as f:
    f.write("Hello")
    f.seek(0)
    f.write("Xa")

# working with binary file
with open("new_wall.jpg", "rb") as f:
    with open("copy_new_wall.jpg", "wb") as wb:
        wb.write(f.read())

"""
# working with other data types
with open('sample.txt','w') as f:
  f.write(5)  # as it is a int so we know that all text is in the form of string
"""

with open("sample.txt", "w") as f:
    f.write(
        "5"
    )  # this is the correct way to do it , i.e no other data type possible to pass

with open("sample.txt", "r") as f:
    print(
        int(f.read()) + 5
    )  # here also the return type of read is in the form of str , so we have to explicitly typecast it to int so that we can able to do arithmetic operation

# more complex data
d = {"name": "nitish", "age": 33, "gender": "male"}

with open("sample.txt", "w") as f:
    f.write(str(d))

"""
with open('sample.txt','r') as f:
  print(dict(f.read()))  #this will through error bcz we cant able to make the dict typecast it to string format
"""

# serialization using json module
# list
import json

L = [1, 2, 3, 4, 5]

with open("demo.json", "w") as f:
    json.dump(L, f)

d = {"name": "sai", "age": 21, "gender": "male"}

with open("demo.json", "w") as f:
    json.dump(d, f, indent=4)

with open("demo.json", "r") as f:
    d = json.load(f)
    print(d)
    print(type(d))

t = (1, 2, 3, 4, 5)
with open("demo.json", "w") as f:
    json.dump(t, f)  # it will store th etuple in the form of list

# What happens when you load it back?
with open("demo.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))

# What if you want the original tuple back?
with open("demo.json", "r") as f:
    data = tuple(json.load(f))

print(data)
print(type(data))

# serializing and deserializing custom object


class Person:

    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender


person = Person("Tanmy", "Nayak", 21, "Male")


# with open("demo.json","w") as f:
# json.dump(person,f) this is not possible to serializable this custom object , it only does mean that we can put readymade python data type into the json file
def show_object(self):
    if isinstance(person, Person):
        return "{} {} age -> {} gender -> {}".format(
            person.fname, person.lname, person.age, person.gender
        )


with open("demo.json", "w") as f:
    json.dump(person, f, default=show_object)


# As a dict
def show_object1(self):
    if isinstance(person, Person):
        return {
            "name": person.fname + " " + person.lname,
            "age": person.age,
            "gender": person.gender,
        }


with open("demo.json", "w") as f:
    json.dump(person, f, default=show_object1, indent=4)

# deserializing
import json

with open("demo.json", "r") as f:
    d = json.load(f)
    print(d)
    print(type(d))


# Pickling
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Hi my name is", self.name, "and I am ", self.age, "years old")


p = Person("nitish", 33)

# pickle dump
import pickle

with open("person.pkl", "wb") as f:
    pickle.dump(p, f)

# pickle load
with open("person.pkl", "rb") as f:
    p = pickle.load(f)

p.display_info()

"""
pickle Vs Json

    Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.
"""
