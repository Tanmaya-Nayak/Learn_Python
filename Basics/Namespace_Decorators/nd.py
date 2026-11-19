###### Namespace & Decorators ######

# local and global
# global var
"""
a = 2

def temp():
    # local var
    b = 3
    print(b)


temp()
print(a)
"""

# local doesnt have but global has
"""
a = 2


def temp():
    print(a)


temp()
print(a)
"""

# Editing global
"""
a = 2


def temp():
    global a
    a += 1
    print(a)


temp()
print(a)
"""


# local and global -> global created inside local
"""
def temp():
    # local var
    global a
    a = 1
    print(a)


temp()
print(a)
"""

# local and global -> function parameter is local
"""
def temp(z):
  # local var
  print(z)

a = 5
temp(5)
print(a)
"""

# built in scope

"""
import builtins

print(dir(builtins))
"""

# Enclosing scope
"""
a = 2
def outer():
  def inner():
    print(a)
  inner()
  print('outer function')


outer()
print('main program')
"""


# Python are 1st class function
"""
def func():
    print("hello")


a = func
a()
# ---------


def modify(funct, num):
    return funct(num)


def square(num):
    return num**2


print(modify(square, 2))
"""


# Decorator simple example
def my_decorator(func):
    def wrapper():
        print("##############")
        func()
        print("##############")

    return wrapper


def hello():
    print("hello")


a = my_decorator(hello)
a()
