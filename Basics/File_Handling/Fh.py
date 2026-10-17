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

# to load a big file in a memory
big_L = ["hello world" for i in range(1000)]

with open("big.txt", "w") as f:
    f.writelines(big_L)

with open("big.txt", "r") as f:
    chunk_size = 10

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end="***")
        f.read(chunk_size)
