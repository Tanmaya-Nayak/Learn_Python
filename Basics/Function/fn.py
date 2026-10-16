# Lets start fn


def is_even(i):  # here i is treated as a parament
    """
    this will return if the no. is even or odd
    input: Any valid integer
    output: odd/even
    """
    if type(i) == int:
        if i % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        print("it must be int type")


for i in range(1, 11):
    x = is_even(i)  # here i is treated as argument
    print(x)

# Types of arguments
# Default Argument
# Positional Argument
# Keyword Argument

# Default Argument


def power(a=1, b=1):
    return a**b


power()  # it will print default 1
power(2)  # it will make a = 2 and b = 1(default)

# Positional Argument
power(2, 3)

# Keyword Argument
power(b=4, a=3)

# *args
# allows us to pass a variable number of non-keyword arguments to a function.


def multiply(*args):
    product = 1
    for i in args:
        product = product * i
    print(args)
    return product


print(multiply(1, 2, 3, 4, 5, 6))

# How to access documentation
print(is_even.__doc__)
print(print.__doc__)
print(type.__doc__)
print(frozenset.__doc__)

# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.


def display(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)


display(india="delhi", srilanka="colombo", nepal="kathmandu", pakistan="islamabad")


# Nested function

"""
def f():
    def g():
        print("Inside function g")
        f()

    g()
    print("Inside function f")


f()
"""
# Functions are 1st class citizen

# type and id


def square(num):
    return num**2


type(square)
id(square)

# Lambda function

# x -> x^2
a = lambda x: x**2
print(a(2))

# x,y -> x+y
s = lambda x, y: x + y
print(s(1, 3))

# check if a string has 'a'
str = lambda x: "a" in x
print(str("sai"))

# odd or Even
is_even = lambda x: "even" if x % 2 == 0 else "odd"
print(is_even(32))

# fetch names from a list of dict

users = [
    {"name": "Rahul", "age": 45, "gender": "male"},
    {"name": "Nitish", "age": 33, "gender": "male"},
    {"name": "Ankita", "age": 50, "gender": "female"},
]

list(map(lambda users: users["gender"], users))

# numbers greater than 5
L = [3, 4, 5, 6, 7]

list(filter(lambda x: x > 5, L))

# fetch fruits starting with 'a'
fruits = ["apple", "guava", "cherry"]

list(filter(lambda x: x.startswith("a"), fruits))

# sum of all item
import functools

functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

# find max
functools.reduce(lambda x, y: x if x > y else y, [23, 11, 45, 10, 1])
