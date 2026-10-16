######OOPs######

# syntax to create an object

#####objectname = classname()

"""
class Atm:
    # constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        user_input = input(
       Hi how can i help you?
       1.Press 1 to create pin
       2.Press 2 to change pin
       3.Press 3 to check balance
       4.Press 4 to withdraw
       5.Anything else to exit
       )

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter ur pin ")
        self.pin = user_pin
        user_balance = int(input("Enter ur balance "))
        self.balance = user_balance
        print("Pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter ur old pin ")

        if old_pin == self.pin:
            print("Enter ur new pin ")
            new_pin = input("Enter ur new pin ")
            self.pin = new_pin
            print("New pin created successfully")
            self.menu()
        else:
            print("Wrong Pin! Access the menue again")
            self.menu()

    def check_balance(self):
        user_pin = print("Enter ur pin ")
        if user_pin == self.pin:
            print("Your balance is ", self.balance)
            self.menu()
        else:
            print("Your entered pin was wrong, Access menu again")
            self.menu()

    def withdraw(self):
        user_pin = print("Enter ur pin ")
        if user_pin == self.pin:
            amount = int(input("Enter ur withdrawn amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("withdrawl successfully. balance is ", self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Wrong Pin")
        self.menu()

"""


class Fraction:

    # parameterized constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        return "{}/{}".format(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        return "{}/{}".format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return "{}/{}".format(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return "{}/{}".format(new_num, new_den)

    def convert_to_decimal(self):
        return self.num / self.den


fr1 = Fraction(3, 4)
fr2 = Fraction(1, 2)

print(fr1)
print(fr1.convert_to_decimal())

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)


class point:

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return "<{},{}>".format(self.x_cord, self.y_cord)

    def euclidean_distance(self, other):
        return (
            (self.x_cord - other.x_cord) ** 2 + (self.y_cord - other.y_cord) ** 2
        ) ** 0.5

    def dist_frm_origin(self):
        return self.euclidean_distance(point(0, 0))


p1 = point(0, 0)
p2 = point(10, 10)

print(p1)
print(p1.euclidean_distance(p2))  # p1 will get automatically passed
print(p2.dist_frm_origin())


class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A, self.B, self.C)

    def point_on_line(line, point):
        if line.A * point.x_cord + line.B * point.y_cord + line.C == 0:
            return "Lies on the line"
        else:
            return "does not lies on the line"

    def shortest_distance(line, point):
        return (
            abs(line.A * point.x_cord + line.B * point.y_cord + line.C)
            / (line.A**2 + line.B**2) ** 0.5
        )


l1 = Line(1, 1, -2)
p3 = point(1, 1)
print(l1)
print(p3)
print(l1.point_on_line(p3))
print(l1.shortest_distance(p3))


class person:
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == "india":
            return "Namaste" + " " + self.name
        else:
            return "Hello" + " " + self.name


p = person("sai", "india")
print(p.name)
print(p.country)
print(p.greet())

# Attribute creation ouside from the class
p.gender = "Male"
print(p.gender)


# pass by reference
class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def greet(person):
        print("Hello i am", person.name, "i am", person.gender)


p = Person("sai", "male")
p.greet()


class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)


class Address:

    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


add1 = Address("Puri", 752002, "odisha")
cust = Customer("sai", "male", add1)

cust.print_address()

cust.edit_profile("sag", "mumbai", 111111, "maharastra")
cust.print_address()

# Inheritance


# constructor example
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 13)
s.buy()

"""
# constructor example 2
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
s.brand
"""

# child can't access private members of the class


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    # getter
    def show(self):
        print(self.__price)


class SmartPhone(Phone):
    def check(self):
        print(self.__price)


s = SmartPhone(20000, "Apple", 13)
s.show()


class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):

    def show(self):
        print("This is in child class")


son = Child(100)
print(son.get_num())
son.show()


class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("class A :", self.var1)


class B(A):

    def display2(self, var1):
        print("class B :", self.var1)


obj = B()
obj.display1(200)


# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")


s = SmartPhone(20000, "Apple", 13)

s.buy()


# using super outside the class
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        # syntax to call parent ka buy method
        super().buy()


s = SmartPhone(20000, "Apple", 13)

s.buy()


# super -> constuctor
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print("Inside smartphone constructor")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")


s = SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)


# practice questions
class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):

    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val


son = Child(100, 200)
print(son.get_num())
print(son.get_val())


# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()


# multilevel
class Product:
    def review(self):
        print("Product customer review")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


class FeaturePhone(Phone):
    pass


SmartPhone(1000, "Apple", "13px").buy()
FeaturePhone(10, "Lava", "1px").buy()


# Multiple
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Product:
    def review(self):
        print("Customer review")


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "Apple", 12)

s.buy()
s.review()


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Product:
    def buy(self):
        print("Product buy method")


# Method resolution order
class SmartPhone(Phone, Product):
    pass


s = SmartPhone(20000, "Apple", 12)

s.buy()


# Polymorphism
class Shape:

    def area(self, a, b=0):
        if b == 0:
            return 3.14 * a * a
        else:
            return a * b


s = Shape()

print(s.area(2))
print(s.area(3, 4))
