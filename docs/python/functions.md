# Functions & Scope

Functions are reusable, isolated blocks of code that accept inputs, execute instructions, and return results. In Python, functions are **first-class citizens**, meaning they can be assigned to variables, passed as arguments, and returned from other functions.

---

## Functions vs Methods

It is important to distinguish between independent functions and object-bound methods:

- **Built-in Functions**: Standalone functions callable globally on any compatible object.
- **Methods**: Functions bound specifically to an object instance or class.

```python
name = "Tanishk"

# Built-in functions (standalone)
print(type(name))   # Returns object class type: <class 'str'>
print(len(name))    # Returns sequence length: 7

# Method (bound to the string object instance)
print(name.upper()) # "TANISHK"
```

---

## Defining & Calling Functions

When Python encounters a `def` statement, it compiles the code block and binds a function object into memory:

```python
# Function Definition
def greet(name):
    """Greets the user by name."""
    print(f"Hello {name}!")

# Function Invocation
greet("Tanishk")
```

**Expected Output:**
```text
Hello Tanishk!
```

---

## Common Function Shapes

Functions in Python generally take one of three design patterns depending on parameters and return semantics:

### 1. No Parameters & No Return Value
```python
def greet():
    print("Hello!")

greet()  # Output: Hello!
```

### 2. Parameters & No Return Value (Side Effect)
```python
def greet(name):
    print(f"Hello {name}!")

greet("Tanishk")  # Output: Hello Tanishk!
```

### 3. Parameters with Explicit Return Value
```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)  # Output: 15
```

::: info Implicit Return Value
If a Python function finishes execution without an explicit `return` statement, it automatically returns `None`.
:::

---

## Parameters vs Arguments

- **Parameters**: The variable names specified in the function signature definition.
- **Arguments**: The actual values or references supplied when calling the function.

### Positional Arguments
Arguments matched purely by their order:

```python
def greet(name, age):
    print(f"Hello {name}!")
    print(f"You are {age} years old.")

greet("Tanishk", 20)
```

### Keyword Arguments
Arguments matched explicitly by parameter name, regardless of order:

```python
greet(age=20, name="Tanishk")
```

### Mixed Arguments
When mixing both styles, **positional arguments must always precede keyword arguments**:

```python
# Valid: positional first, followed by keyword
greet("Tanishk", age=20)

# SyntaxError: positional argument follows keyword argument
# greet(name="Tanishk", 20)
```

---

## Default Parameter Values

Parameters can have fallback values used if no argument is supplied at invocation:

```python
def display(name="Tanishk"):
    print(f"User: {name}")

display()          # Output: User: Tanishk
display("Alex")    # Output: User: Alex
```

::: warning Mutable Default Argument Gotcha
Never use mutable objects (like `[]` or `{}`) as default parameters. Since function defaults are evaluated once at definition time, state persists across invocations. Instead, use `None`:
```python
def add_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```
:::

---

## Variable-Length Arguments: `*args` and `**kwargs`

When the exact number of incoming arguments is dynamic or unknown, use `*args` and `**kwargs`:

### 1. Positional Variable Arguments: `*args`
Packs arbitrary positional arguments into a `tuple`:

```python
def total(*args):
    # args is a tuple: (1, 2, 3, ...)
    return sum(args)

print(total(1, 2))          # 3
print(total(1, 2, 3))       # 6
print(total(1, 2, 3, 4, 5)) # 15
```

### 2. Keyword Variable Arguments: `**kwargs`
Packs arbitrary named keyword arguments into a `dict`:

```python
def create_user(**kwargs):
    # kwargs is a dictionary: {'first_name': 'Mo', 'age': 34, ...}
    print(kwargs)

create_user(first_name="Mo", age=34, country="Africa")
```

**Expected Output:**
```text
{'first_name': 'Mo', 'age': 34, 'country': 'Africa'}
```

::: tip When to Use Which?
- Use `*args` when passing sequences of homogeneous values (e.g. lists of numbers).
- Use `**kwargs` when handling structured metadata or optional configuration flags.
:::

---

## Type Hints & Annotations

Python supports optional type annotations (PEP 484) to improve code documentation, auto-completion, and static analysis:

```python
def calculate_discount(price: float, discount: float) -> float:
    return price ** discount
```

::: info Runtime Enforcement
Type hints are **not** enforced at runtime by the Python interpreter. They serve as contracts for developers, IDEs, and static analysis tools like `mypy`.
:::

---

## Summary Reference

| Syntax | Mechanism | Type Created |
| :--- | :--- | :--- |
| `def fn(a, b):` | Positional parameters | Standard local bindings |
| `def fn(a=1):` | Default fallback argument | Evaluated at definition |
| `def fn(*args):` | Variable positional arguments | `tuple` |
| `def fn(**kwargs):` | Variable keyword arguments | `dict` |
| `def fn(a: int) -> int:` | Function type annotations | Introspection metadata |
