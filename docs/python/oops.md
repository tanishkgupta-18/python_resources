# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **data (attributes)** and **behavior (methods)** rather than functions and logic alone.

In Python, **everything is an object**, and OOP provides the architecture for writing modular, reusable, and maintainable software.

---

## 1. Classes, Objects & The `self` Parameter

- **Class**: A blueprint or prototype from which individual objects are created.
- **Object (Instance)**: A concrete instance of a class with its own state and allocated memory.
- **`self`**: A reference to the **current instance** of the class. It allows methods to access and modify the specific object's attributes and methods.

```python
class Car:
    # Class variables (shared across all instances)
    brand = "Audi"
    wheels = 4

    # Instance methods (always take 'self' as the first parameter)
    def accelerate(self):
        print("accelerate")

    def brake(self):
        print("brake")

# Instantiating an object
car = Car()

print(car.brand)    # Output: Audi
print(car.wheels)   # Output: 4
car.accelerate()    # Output: accelerate
car.brake()         # Output: brake
```

::: tip Why is `self` Required?
When you call `car.accelerate()`, Python automatically converts it under the hood to `Car.accelerate(car)`. Passing `self` explicitly ensures the method knows precisely which instance it is operating upon.
:::

---

## 2. Constructors (`__init__`) & Object Lifecycle

The `__init__()` method is Python's built-in **constructor**. It is automatically executed when a new instance of a class is instantiated.

### Object Creation Flow
1. **Memory Allocation**: Python allocates a memory address for the new object.
2. **`__init__()` Invocation**: The constructor executes automatically to initialize instance variables.
3. **State Binding**: Values are bound to `self.<variable_name>`.

```python
class Student:
    def __init__(self, name, roll_no, marks):
        # Instance variables (unique to each student instance)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def printHello(self):
        print(f"Hello, {self.name}!")

# Instantiation with parameters
s1 = Student("krish", 21, 95)
s1.printHello()  # Output: Hello, krish!
```

::: warning No Multiple Constructors in Python
Python **does not support constructor or method overloading by signature**. If you define multiple `__init__()` methods in the same class, the last definition will overwrite all preceding ones!
:::

---

## 3. Simulating Constructor Overloading

Because Python does not support multiple constructors natively, we use two idiomatic approaches to achieve constructor flexibility:

### Approach 1: Default Arguments (Recommended)

Using default values (`None` or sensible defaults) lets callers invoke the constructor with varying numbers of arguments:

```python
class Student:
    def __init__(self, name=None, age=None):
        if name is None and age is None:
            print("Default constructor")
        elif age is None:
            print("Name constructor")
        else:
            print("Name and age constructor")

s1 = Student()            # Output: Default constructor
s2 = Student("Rahul")     # Output: Name constructor
s3 = Student("Rahul", 22) # Output: Name and age constructor
```

### Approach 2: Variable-Length Arguments (`*args`)

Using `*args` allows dynamic parameter handling based on length inspection:

```python
class Calculator:
    def __init__(self, *args):
        if len(args) == 0:
            print("No arguments")
        elif len(args) == 1:
            print("One argument:", args[0])
        elif len(args) == 2:
            print("Two arguments:", args[0], args[1])

c1 = Calculator()        # Output: No arguments
c2 = Calculator(10)      # Output: One argument: 10
c3 = Calculator(10, 20)  # Output: Two arguments: 10 20
```

---

## 4. The Four Pillars of OOP

<div class="pillars-grid">
  <div class="pillar-card">
    <div class="pillar-header">
      <span class="pillar-num">Pillar 01</span>
      <span class="pillar-tag">Data Protection</span>
    </div>
    <h4>Encapsulation</h4>
    <p>Binds data attributes and methods together into a protective unit while restricting direct external access.</p>
  </div>

  <div class="pillar-card">
    <div class="pillar-header">
      <span class="pillar-num">Pillar 02</span>
      <span class="pillar-tag">Hide Complexity</span>
    </div>
    <h4>Abstraction</h4>
    <p>Hides internal implementation details and exposes only the essential public interface via abstract base classes.</p>
  </div>

  <div class="pillar-card">
    <div class="pillar-header">
      <span class="pillar-num">Pillar 03</span>
      <span class="pillar-tag">Code Reuse</span>
    </div>
    <h4>Inheritance</h4>
    <p>Allows a child class to acquire attributes and methods from parent classes, eliminating duplicate logic.</p>
  </div>

  <div class="pillar-card">
    <div class="pillar-header">
      <span class="pillar-num">Pillar 04</span>
      <span class="pillar-tag">Multiple Forms</span>
    </div>
    <h4>Polymorphism</h4>
    <p>Enables a unified method or operator to exhibit different behaviors across distinct object types.</p>
  </div>
</div>

---

## 5. Encapsulation: Data Protection & Access Control

**Encapsulation** bundles data (attributes) and methods together into a single unit while restricting direct outside access to internal state.

In Python:
- **Public**: `self.name` (accessible anywhere).
- **Private**: `self.__password` (prefixed with double underscores `__`, triggering name mangling).

### Classical Getters & Setters

```python
class BankAccount:
    def __init__(self, name, password, balance):
        self.name = name
        self.__password = password  # Private attribute
        self.__balance = balance    # Private attribute

    # Getter: Controlled read access
    def getBalance(self):
        return self.__balance

    # Setter: Controlled write access with validation
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

print("Current Balance:", account.getBalance())  # Output: 5000
account.deposit(1000)                            # Output: Amount Deposited, Updated Balance is: 6000
account.withdraw(2000)                           # Output: Amount Withdrawn, Updated Balance is: 4000
account.setPassword("5678")                      # Output: Password Updated Successfully!
```

### Pythonic Property Decorator (`@property`)

Python provides the `@property` decorator to access and mutate private attributes using standard attribute syntax, while still executing validation logic behind the scenes:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    # Getter property
    @property
    def marks(self):
        return self.__marks

    # Setter property
    @marks.setter
    def marks(self, new_marks):
        if new_marks < 0 or new_marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = new_marks

s = Student("Tanishk", 90)

# Accessed like a normal attribute, but calls the getter method
print(s.marks)  # Output: 90

# Mutated like a normal attribute, but executes the setter method
s.marks = 95
print(s.marks)  # Output: 95
```

---

## 6. Abstraction: Hiding Complexity

**Abstraction** hides internal implementation complexities and reveals only the essential interface to the user.

Python implements abstraction via the `abc` (Abstract Base Class) module:
- Inherit from `ABC`.
- Decorate required abstract methods with `@abstractmethod`. Subclasses **must** provide concrete implementations, or Python raises a `TypeError` at instantiation.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        """Every vehicle must define its own engine implementation."""
        pass

class Car(Vehicle):
    def engine(self):
        print("How car engine works: Internal Combustion / Electric Drivetrain")

class Bike(Vehicle):
    def engine(self):
        print("How bike engine works: Two-stroke / Four-stroke compact engine")

car = Car()
bike = Bike()

car.engine()   # Output: How car engine works: Internal Combustion / Electric Drivetrain
bike.engine()  # Output: How bike engine works: Two-stroke / Four-stroke compact engine
```

::: info Enforcement at Instantiation
If a subclass does not implement all abstract methods, attempting to instantiate it raises `TypeError: Can't instantiate abstract class with abstract methods`.
:::

---

## 7. Inheritance: Code Reuse & Hierarchy

Inheritance allows a child class to inherit attributes and methods from a parent class, eliminating code duplication and enabling hierarchical modeling.

### Single Inheritance & `super()`

Use `super()` to invoke parent constructors and methods cleanly:

```python
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def address(self):
        print("Headquarters: Los Angeles")

    def getName(self):
        return self.company_name

class Employee(Company):
    def __init__(self, name, emp_id, company_name):
        self.name = name
        self.id = emp_id
        # Call parent class constructor
        super().__init__(company_name)

    def work(self):
        print("Role: Software Engineer")

    def getDetails(self):
        print(f"Company: {super().getName()}, Employee: {self.name}")

emp = Employee("Rohan", 123, "XYZ Tech")
emp.work()        # Output: Role: Software Engineer
emp.address()     # Output: Headquarters: Los Angeles
emp.getDetails()  # Output: Company: XYZ Tech, Employee: Rohan
```

### Multiple Inheritance

A class can inherit directly from more than one parent:

```python
class Father:
    def drive(self):
        print("Father Drives")

class Mother:
    def cook(self):
        print("Mother Cooks")

class Child(Father, Mother):
    pass

ch = Child()
ch.drive()  # Output: Father Drives
ch.cook()   # Output: Mother Cooks
```

### Hybrid Inheritance & Method Resolution Order (MRO)

When multiple or diamond inheritance trees are formed, Python resolves method lookup using **Method Resolution Order (MRO)** based on the **C3 Linearization Algorithm**:

```python
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

b = Bat()
b.eat()    # Inherited from Animal via Mammal
b.walk()   # Inherited from Mammal
b.fly()    # Inherited from Bird
b.sleep()  # Own method
```

### MRO Conflict Resolution

If multiple parents define a method with the identical name, Python resolves from left to right as specified in the class definition list:

```python
class Father:
    def drive(self):
        print("Father Drives")

class Mother:
    def drive(self):
        print("Mother Drives")

class Child(Father, Mother):
    pass

ch = Child()
ch.drive()  # Output: Father Drives (Father appears before Mother in Child definition)

# Inspecting the exact lookup sequence:
print(Child.mro())
# [Child, Father, Mother, object]
```

---

## 8. Polymorphism: Flexibility & Magic Methods

Polymorphism ("many forms") allows different classes to share identical method signatures while delivering customized behaviors.

### 1. Method Overriding (Runtime Polymorphism)

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Polymorphic dispatcher function (Duck Typing)
def make_sound(animal):
    animal.sound()

make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow
```

---

### 2. Operator Overloading with Magic (Dunder) Methods

Operator overloading allows user-defined objects to interact with standard Python operators (`+`, `-`, `*`, `==`, etc.) through special double-underscore ("dunder") methods.

#### Example: Complex Number Addition

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the '+' operator
    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def display(self):
        print(f"{self.real} + {self.imag}i")

c1 = Complex(10, 20)
c2 = Complex(30, 40)

# Uses __add__ under the hood
c3 = c1 + c2
c3.display()  # Output: 40 + 60i
```

#### Example: Custom Numeric Wrapper

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(10)
n2 = Number(20)
n3 = n1 + n2

print(n3.value)  # Output: 30
```

---

## Complete Magic Methods Reference Table

| Operator | Dunder Method | Operation |
| :--- | :--- | :--- |
| `+` | `__add__(self, other)` | Addition |
| `-` | `__sub__(self, other)` | Subtraction |
| `*` | `__mul__(self, other)` | Multiplication |
| `/` | `__truediv__(self, other)` | Floating-point division |
| `//` | `__floordiv__(self, other)` | Integer floor division |
| `%` | `__mod__(self, other)` | Modulo remainder |
| `**` | `__pow__(self, other)` | Exponentiation |
| `==` | `__eq__(self, other)` | Equality test |
| `!=` | `__ne__(self, other)` | Inequality test |
| `<` | `__lt__(self, other)` | Less than |
| `>` | `__gt__(self, other)` | Greater than |
| `<=` | `__le__(self, other)` | Less than or equal |
| `>=` | `__ge__(self, other)` | Greater than or equal |
| `len()` | `__len__(self)` | Container length |
| `str()` | `__str__(self)` | User-friendly string representation |
| `repr()` | `__repr__(self)` | Unambiguous debug string representation |

---

## Summary Reference

| Concept | Key Syntax / Construct | Main Purpose |
| :--- | :--- | :--- |
| **Class & Object** | `class Car: ...`, `c = Car()` | Blueprint and instance creation |
| **Constructor** | `def __init__(self, ...):` | Automatic object initialization |
| **Encapsulation** | `self.__private_var`, `@property` | Data protection and controlled access |
| **Abstraction** | `class Base(ABC): @abstractmethod` | Defining interfaces and enforcing contracts |
| **Inheritance** | `class Child(Parent):`, `super()` | Code reuse, specialization, and hierarchies |
| **MRO** | `Class.mro()`, C3 Linearization | Predictable multi-parent method lookup |
| **Polymorphism** | Method Overriding, `def __add__` | Unified interface across diverse data types |
