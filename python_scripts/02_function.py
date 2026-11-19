# functions are independent blocks of code whereas methods are function that are associated with an object.

# BUILT-IN FUNCTIONS

name = "Tanishk"
print(type(name)) # type() is a built-in function that returns the type of the object passed to it.
print(len(name)) # len() is a built-in function that returns the length of the object passed to it.
# method
print(name.upper()) # upper() is a built-in method that returns the string in uppercase.

# user-defined function

# function definition
def greet(name):
    print(f"Hello {name}!") # description of the function

# function call
greet("Tanishk") # Output: Hello Tanishk!

# python reads the function definition and creates a function object in memory. When the function is called, the code inside the function is executed.

# function shapes

# 1. Function with no parameters and no return value
def greet():
    print("Hello!") # description of the function

greet() # Output: Hello!

# 2. Function with parameters and no return value

def greet(name):
    print(f"Hello {name}!") # description of the function

greet("Tanishk") # Output: Hello Tanishk!

# 3. Function with parameters and return value

def add(a, b):
    return a + b # description of the function

result = add(5, 10) # Output: 15

# Parameters and Arguments

# Parameters are the variables that are defined in the function definition. Arguments are the values that are passed to the function when it is called.

# def function_name(parameter1, parameter2):
#     # function body
#     pass

# function_name(argument1, argument2) # calling the function with arguments

# postional arguments are the arguments that are passed to the function in the order in which they are defined in the function definition.
# Keyword arguments are the arguments that are passed to the function with the name of the parameter.

# for example

def greet(name, age):
    print(f"Hello {name}!")
    print(f"You are {age} years old.")


# postional arguments
greet("Tanishk", 20) # Output: Hello Tanishk! You are 20 years old. 

# keyword arguments
greet(age=20, name="Tanishk") # Output: Hello Tanishk! You are 20 years old.

# mixed arguments

# you must start with postional
greet("Tanishk", age=20) # Output: Hello Tanishk!

# default parameter -> its a default value if nothing is passed

# def display(name = "Tanishk")


# *args and **kwargs

# allows functions to accepts a unknown number of arguments

# * for positional arguments and ** keyword arguments

# def total(a, b):
#     return a+b

# total(1, 2)
# total(1, 2, 3)
# total(1,2,3,4)

# ...so on


# args classtype is tuple
def total(*args):
    return sum(args)

total(1, 2)
total(1, 2, 3)
total(1,2,3,4)

# ... so on


# when you pass similar values use *args
(1,2,3,4,5)
# when you pass different values use **kwargs

("alex", 24, "Los Angeles", 10-11-2026)

#create user profile
def create_user(**kwargs):
    print(kwargs)

create_user(first_name = "Mo", age = 34, country = "Africa")

# Type Hints

def calculate_discount(price: float, discount: float)->float:
    return price**discount;

# type hints are for us not for python -> float means what it returns (returned data type)
