# How to handle exception in python
# Try except block

# Lets create a file
with open("sample.txt", "w") as f:
    f.write("Hello world")

try:
    with open("sample1.txt", "r") as f:
        print(f.read())
except:
    print("File not found")

# catch specific exception
try:
    m = 5
    with open("sample.txt", "r") as f:
        print(f.read())

    print(m)
    print(5 / 2)
    L = [1, 2, 3, 4]
    L[100]
except FileNotFoundError:
    print("File not found")
except NameError:
    print("Variable not defined")
except ZeroDivisionError:
    print("Cant divide by 0")
except Exception as e:
    print(e)

# else
try:
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("file not found")
except Exception:
    print("something fishy")
else:
    print(f.read())
    f.close()


# Finally
try:
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("file not found")
except Exception:
    print("something fishy")
else:
    print(f.read())
finally:
    f.close()
    print("file closed")

# Raise exception
"""
raise ZeroDivisionError("just trying exception")
raise NameError("Just Try")
raise TypeError("try")
"""


class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.amount = amount

        if amount < 0:
            raise Exception("Amount cant be -ve")
        if self.balance < amount:
            raise Exception("U dont have money")
        self.balance = self.balance - self.amount


obj = Bank(10000)

try:
    obj.withdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)


# creating custom exceptions
# exception hierarchy in python


# simple example
class SecurityError(Exception):

    def __init__(self, message):
        print(message)

    def logout(self):
        print("logout")


class Google:

    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if self.device != device:
            raise SecurityError("Teri to lag gayi")
        if email == self.email and password == self.password:
            print("Welcome")
        else:
            print("login Error")


obj = Google("nitish", "nitish@gmail.com", "1234", "android")

try:
    obj.login("nitish@gmail.com", "1234", "windows")
except SecurityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print("database connection closed")
