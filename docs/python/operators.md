# Logic & Operators

Logic, comparison, and identity operators dictate how conditions evaluate in Python. Understanding the difference between equality (`==`) and identity (`is`), as well as short-circuit boolean logic, is essential for writing bug-free code.

---

## Boolean Expressions & Truthiness

In Python, truth values are represented by the `bool` type (`True` and `False`). Every Python object has an implicit truth value when passed into `bool()`:

```python
# Non-zero numbers and non-empty sequences evaluate to True
print(bool(123))    # True
print(bool("Hi"))   # True

# Zero, None, and empty containers evaluate to False
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False
```

---

## Chained Comparisons

Python supports intuitive mathematical chained comparisons without repeating operands:

```python
# Chained comparison: equivalent to (1 < 2) and (2 < 4)
print(1 < 2 < 4)  # True

age = 18
# Tests whether age is in the range [18, 30]
print(18 <= age <= 30)  # True
```

---

## Logical Operators (`and`, `or`, `not`)

Python uses readable keywords rather than symbols for logical operations:

```python
age = 18

# 'and' requires both conditions to be True
print(age >= 18 and age <= 30)  # True

# 'or' requires at least one condition to be True
print(age <= 18 or age >= 30)   # True

# 'not' inverts the truth value
print(not (age == 18))          # False
```

::: tip Operator Precedence
`not` has the highest priority among logical operators, followed by `and`, then `or`. Use parentheses `()` whenever combining expressions to ensure unambiguous execution order:
```python
# 'and' executes before 'or'
result = True or False and False  # Evaluates to True (False and False -> False; True or False -> True)
```
:::

---

## Membership Operators (`in`, `not in`)

The `in` and `not in` operators test for sequence membership (strings, lists, tuples, sets, dictionaries):

```python
text = "Data"

print("a" in text)      # True
print("a" not in text)  # False
```

---

## Identity (`is`) vs Equality (`==`)

One of the most important distinctions in Python is value equality versus object identity:

- **`==` (Equality)**: Compares whether two objects have the same **value**.
- **`is` (Identity)**: Compares whether two variables reference the exact same **object in memory** (`id(a) == id(b)`).

### 1. Mutable Objects (e.g., Lists)

```python
# Two separate lists created independently in memory
a = [1, 2, 4]
b = [1, 2, 4]

print(a == b)  # True  -> Values are identical
print(a is b)  # False -> Distinct objects in memory (different IDs)

# Assigning b to a makes both point to the same memory location
a = b
print(a is b)  # True  -> Both reference the same memory address
```

### 2. Primitive Values & Small Integer Caching

For immutable primitives like small integers (typically -5 to 256) and short strings, Python reuses internal objects:

```python
a = 5
b = 5
print(a is b)  # True (Python caches small integers to optimize memory)
```

---

## `None` vs Empty String `""`

```python
# None represents an unknown or unassigned state
# "" represents a known, defined string with zero length

email = None

# Idiomatic check for None in Python: always use 'is'
print(email is None)      # True
print(email is not None)  # False
```

::: warning Use `is` with Singletons
Because `None`, `True`, and `False` are singletons in Python, always compare them using `is` and `is not` instead of `==` or `!=`.
:::

---

## Summary Reference

| Operator | Type | Behavior | Example |
| :--- | :--- | :--- | :--- |
| `==` | Equality | True if operand values are equal | `[1] == [1]` -> `True` |
| `!=` | Inequality | True if operand values differ | `1 != 2` -> `True` |
| `is` | Identity | True if operands share identical memory address | `x is None` |
| `is not` | Identity | True if operands point to different objects | `x is not None` |
| `in` | Membership | True if element exists inside container | `"p" in "python"` |
| `not in` | Membership | True if element is absent | `5 not in [1, 2]` |
| `and` | Logical | Short-circuit AND | `True and False` -> `False` |
| `or` | Logical | Short-circuit OR | `False or True` -> `True` |
| `not` | Logical | Boolean negation | `not True` -> `False` |
