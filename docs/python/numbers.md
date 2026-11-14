# Numbers & Arithmetic

Python offers built-in support for numeric operations, including standard integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`), alongside the standard `math` and `random` libraries.

---

## Numeric Types & Type Casting

Python dynamically types numeric values, but explicit conversions can be performed using conversion functions:

```python
# Floating-point to integer (truncates towards zero)
x = 3.14
print(int(x))  # 3

# Integer to float
y = 3
print(float(y))  # 3.0

# Creating complex numbers
p = 3
q = 4
z = complex(p, q)
print(z)  # (3+4j)
```

---

## Arithmetic Operators: Division & Exponents

Python distinguishes between standard float division and floor division:

```python
# Standard Division (/) always returns a float
print(7 / 2)   # 3.5

# Floor Division (//) rounds down to the nearest integer
print(7 // 2)  # 3

# Exponentiation (**) raises base to power
print(2 ** 3)  # 8 (2 * 2 * 2)
```

::: info Division Difference
- `/` performs true division: `4 / 2` yields `2.0` (float).
- `//` performs floor division: `7 // 2` yields `3` (int).
:::

---

## Built-in Math Functions

Python provides built-in utilities for magnitude and rounding without needing any external imports:

```python
# Absolute value
x = -3
print(abs(x))  # 3

# Rounding to specified decimal places
price = 35.34567
print(round(price, 3))  # 35.346
```

::: tip Banker's Rounding in Python
In Python 3, `round()` uses **half to even** (Banker's rounding). For exact half-way ties (e.g., `1.5`, `2.5`), Python rounds to the nearest even number:
```python
print(round(1.5))  # 2
print(round(2.5))  # 2
```
:::

---

## The `math` Module: Rounding & Truncation

For granular control over ceiling, floor, and truncation operations, use Python's built-in `math` module:

```python
import math

price = 35.34567

# math.ceil() rounds UP to the nearest integer
print(math.ceil(price))   # 36

# math.floor() rounds DOWN to the nearest integer
print(math.floor(price))  # 35

# math.trunc() eliminates the fractional component, returning the integer part
print(math.trunc(price))  # 35
```

---

## Random Number Generation

The `random` module provides tools for generating pseudorandom numbers:

```python
import random

# Floating-point random number in the range [0.0, 1.0)
print(random.random())

# Random integer between 1 and 6 inclusive (e.g. dice roll)
print(random.randint(1, 6))
```

---

## Numeric Inspection & Type Checks

Python provides methods to verify whether a float has an integer value, as well as strict type validation:

```python
x = 7.0
y = 7.1

# .is_integer() checks if the float value has zero fractional part
print(x.is_integer())  # True
print(y.is_integer())  # False

# isinstance() validates the exact type
print(isinstance(x, int))    # False (x is a float: 7.0)
print(isinstance(x, float))  # True
```

---

## Quick Reference Table

| Operation | Syntax | Description | Example Result |
| :--- | :--- | :--- | :--- |
| True Division | `a / b` | Float result | `7 / 2 -> 3.5` |
| Floor Division | `a // b` | Rounded-down integer | `7 // 2 -> 3` |
| Exponentiation | `a ** b` | Power computation | `2 ** 3 -> 8` |
| Absolute Value | `abs(x)` | Distance from zero | `abs(-5) -> 5` |
| Round | `round(val, n)` | Nearest value (half to even) | `round(3.1415, 2) -> 3.14` |
| Ceiling | `math.ceil(x)` | Smallest integer `>= x` | `math.ceil(3.2) -> 4` |
| Floor | `math.floor(x)` | Largest integer `<= x` | `math.floor(3.8) -> 3` |
| Truncate | `math.trunc(x)` | Discards decimal part | `math.trunc(3.9) -> 3` |
| Random Float | `random.random()` | Value in `[0.0, 1.0)` | e.g. `0.482...` |
| Random Int | `random.randint(a, b)` | Integer in `[a, b]` inclusive | e.g. `1 <= n <= 6` |
| Integer Check | `float.is_integer()` | True if fractional part is `0` | `(4.0).is_integer() -> True` |
