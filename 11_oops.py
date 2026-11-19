# CLASS AND OBJECTS
class Car:
    # variables
    brand = "Audi"
    wheels = 4

    # functions
    def accelerate(self):
        print("accelerate")
    def brake(self):
        print("brake")

car = Car()
print(car.brand)
print(car.wheels)
car.accelerate()
car.brake()

# CONSTRUCTOR

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def printHello(self):
        print("hello!")

s1 = Student("krish", 21, 95)

# NOTES:

# constructor in python always named as __init__()
# when you write any function of class always use self as first parameter
# self points out the current object or instance for which the function or the constructor has been called.
# self refers to the current object
# self used to access instance variables and methods of the current object.

# Object creation flow:
# Memory is allocated for the object
# __init()__ is automatically called
# data is stored inside object

# python cannot have multiple constructors and also does not suppor method overloading.
# therefore only one constructor or init is there and if you try to define new it replaces the old.
# two types of constructor default and parameterized.

# How does Python achieve constructor overloading?

# Approach 1: Default arguments(Most Common)

class Student:
    def __init__(self, name=None, age=None):
        if name is None and age is None:
            print("Default constructor")

        elif age is None:
            print("Name constructor")

        else:
            print("Name and age constructor")


s1 = Student()
s2 = Student("Rahul")
s3 = Student("Rahul", 22)

# Approach 2: *args

class Calculator:
    def __init__(self, *args):
        if len(args) == 0:
            print("No arguments")

        elif len(args) == 1:
            print("One argument:", args[0])

        elif len(args) == 2:
            print("Two arguments:", args[0], args[1])


c1 = Calculator()
c2 = Calculator(10)
c3 = Calculator(10, 20)

# FOUR PILLARS OF OOPS


# ENCAPSULATION: data protection
# ABSTRACTION: hides complexity
# INHERITANCE: code reusability
# POLYMORPHISM: flexibility

# ============================= ENCAPSULATION ================================
# Encapsulation: is the process of binding data and methods together and restricting direct access to data

# capsule: everything packed inside safely data and methods


class BankAccount:
    def __init__(self, name, __password, __balance):
        self.name = name
        self.__password = __password
        self.__balance = __balance

    # Getter
    def getBalance(self):
        return self.__balance

    # Setter
    def setPassword(self, new_password):
        self.__password = new_password
        print("Password Updated Successfully!")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.__balance += amount
        print("Amount Deposited, Updated Balance is:", self.__balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if self.__balance < amount:
            print("Insufficient Balance")
            return

        self.__balance -= amount
        print("Amount Withdrawn, Updated Balance is:", self.__balance)


account = BankAccount("Rahul", "1234", 5000)

print("Current Balance:", account.getBalance())

account.deposit(1000)
account.withdraw(2000)
account.setPassword("5678")

# how to access a private variable without calling a function
class Student:
    def __init__(self, name, __marks):
        self.name = name
        self.__marks = __marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_marks):
        self.__marks = new_marks

# @property we can access a variable as a function
# we can both access and update
# benefits?

# =================================== ABSTRACTION ===============================

# Abstraction is the process of hiding internal implementation details and showing only essential functionality to the user

# for example you can withdraw and check balance in atm but cannot see behind server logics and processing
from abc import abstractmethod, ABC
class Vehicle(ABC):
    @abstractmethod
    # customers knows that it has engine but what going behind it or how it works
    def engine(self): 
        pass

class Car(Vehicle):
    def engine(self):
        print("How car engine works")

class Bike(Vehicle):
    def engine(self):
        print("how bike engine works")

# ABC : abstract base class
# abstractmethod : decorator

# ====================================== INHERITANCE ============================

class Bird:
    def eat(self):
        print("Eat")
    def fly(self):
        print("Fly")

class Dog:
    def eat(self):
        print("Eat")
    def fly(self):
        print("Fly")

class Fish:
    def eat(self):
        print("Eat")
    def fly(self):
        print("Fly")

# Problem with this code is duplication.If you make a change to one function you have to make in all.

# Inheritance is a mechanism where child class acquires properties and methods of a parent class

# code reusability, better organization and less duplication

class Animal:
    def eat(self):
        print("Eat")


class Bird(Animal):
    def fly(self):
        print("Fly")


class Dog(Animal):
    pass


class Fish(Animal):
    pass


# Objects
b = Bird()
d = Dog()
f = Fish()

b.eat()
b.fly()

d.eat()
f.eat()

# Single Inheritance

class Company:
    def __init__(self, company_name):
        self.company_name = company_name
    def address(self):
        print("Los Angeles")

    def getName(self):
        return self.company_name
    
class Employee(Company):
    def __init__(self, name, id, company_name):
        self.name = name
        self.id = id
        super().__init__(company_name) # from this can call constructor of parent
    def work(self):
        print("SWE")

    def getName(self):
        print(super.getName())
        return self.name

emp = Employee("Rohan", 123, "XYZ")
emp.work()
emp.address()

# Super Keyword

#super() is used to call methods or constructors of the parent class from the child class

# avoid code duplication
# ensures parent initialization
# works correctly with multiple inheritance

# =================================== MULTIPLE INHERITANCE ====================

class Father:
    def drive(self):
        print("Drive")

class Mother:
    def cook(self):
        print("Cook")

class Child(Father, Mother):
    pass

ch = Child()
ch.drive()
ch.cook()

# ==================== Hybrid Inheritance ================================
class Animal:
    def eat(self):
        print("Eating")


class Mammal(Animal):
    def walk(self):
        print("Walking")


class Bird(Animal):
    def fly(self):
        print("Flying")


class Bat(Mammal, Bird):
    def sleep(self):
        print("Sleeping")


# Object
b = Bat()

b.eat()
b.walk()
b.fly()
b.sleep()

class Father:
    def drive(self):
        print("Father Drives")

class Mother:
    def drive(self):
        print("Mother Drives")

# here are three drive function two are inherited and 1 its own
class Child(Father, Mother):
    def drive(self):
        print("Child Drives")

ch = Child()
ch.drive()

# Which drive function will be used?

# MRO - Method Resolution Order : is the order in which python searches for a method when a method is called on an object

# Python uses C3 linearization algorithm
# ensure left to right order, no parent is skipped and consistent hiereachy

# it will call Father's drive since its in the left of definition in child 

# ============================== POLYMORPHISM ================================

# polymorphism means many forms - the same method name behaves differently in different situations

# one interface, multiple behaviours

# compile time polymorphism
# function overloading (Not possible in python)
# runtime polymorphism - function overriding

# Method Overriding

# When a child class provides its own implementation of a method already defined in the parent class

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Objects
a1 = Dog()
a2 = Cat()

a1.sound()
a2.sound()

# Same parent type and different objects
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())

# Operator Overloading

# Operator Overloading in Python is another form of polymorphism where we define how operators (+, -, *, ==, etc.) behave for user-defined objects.

# Python achieves operator overloading using special methods (magic methods / dunder methods).
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def display(self):
        print(f"{self.real} + {self.imag}i")


c1 = Complex(10, 20)
c2 = Complex(30, 40)

c3 = c1 + c2

c3.display()


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2

print(n3.value)

# Operator	Magic method
# +	__add__()
# -	__sub__()
# *	__mul__()
# /	__truediv__()
# //	__floordiv__()
# %	__mod__()
# ==	__eq__()
# <	__lt__()
# >	__gt__()
# <=	__le__()
# >=	__ge__()