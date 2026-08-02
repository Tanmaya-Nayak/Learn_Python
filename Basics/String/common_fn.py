print(len("hello world"))
print(min("hello world"))
print(max("hello world"))
print(sorted("hello world"))
print(sorted("hello world", reverse=True))

# capitalize/title/upper/lower/swapcase
s = "hello world"
print(s.capitalize())
print(s.title())
print(s.upper())
print("Hello World".lower())
print("HeLlo WorLD".swapcase())

# count/find/index
print("my name is sai".count("i"))
print("my name is sai".find("is"))
print("my name is sai".find("x"))  # -1
print("my name is sai".index("is"))
# print("my name is sai".index("x"))  # error

# endswith/startswith
print("my name is sai".startswith("my"))
print("my name is sai".endswith("ai"))

# format
name = "Nitish"
gender = "Male"
print("my name is {} and i am a {}".format(name, gender))
print("my name is {1} and i am a {0}".format(gender, name))

# isalnum/isalpha/isdigit/isidentifier
print("nitish1234".isalnum())
print("nitish1234".isalpha())
print("nitish1234".isdigit())
print("nitish1234".isidentifier())

# split/join
print("my name is sai".split())
print("".join(["my", "name", "is", "sai"]))

# replace
print("my name is sai".replace("sai", "Tanmy"))

# strip
print("sai              ".strip())
