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
