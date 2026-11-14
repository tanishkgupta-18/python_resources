# Strings & Text Processing

Strings (`str`) in Python are immutable sequences of Unicode characters. Python offers a rich set of built-in methods for formatting, slicing, searching, and validating text.

---

## Type Conversion & String Concatenation

Convert non-string values into strings using the `str()` built-in function:

```python
age = 24
print(type(str(age)))  # <class 'str'>

# Concatenation with the + operator requires explicit string conversion
print("My age is " + str(age) + " years old.")
```

---

## Measuring Length & Counting Occurrences

### 1. The `len()` Function
The `len()` built-in counts every character, including whitespaces and special symbols:

```python
password = "123a"
print(len(password))  # 4
```

### 2. The `.count()` Method
Counts the non-overlapping occurrences of a substring. Python strings are **case-sensitive**:

```python
text = "My name is Name your name is name"

# "name" appears 3 times in lowercase ("Name" with a capital N is excluded)
print(text.count("name"))  # 3
```

---

## Substring Replacement & Chaining

The `.replace(old, new)` method replaces occurrences of a substring and returns a new string:

```python
# Decimal separator conversion
num = "123,23"
print(num.replace(",", "."))  # "123.23"

# Stripping hyphens from phone numbers
phone = "199-234-4566"
print(phone.replace("-", ""))  # "1992344566"

# Method chaining to clean price symbols
price = "$123-23-67"
cleaned_price = price.replace("$", "").replace("-", ",")
print(cleaned_price)  # "123,23,67"
```

---

## String Formatting: f-strings vs Concatenation

Introduced in Python 3.6, **f-strings (Formatted String Literals)** are the modern, readable, and performant standard for string interpolation.

```python
name = "Tanishk"
age = 24
is_student = True

# Old concatenation approach (verbose and manual)
print("Student Name: " + str(name) + " is " + str(age) + " years old " + "student status: " + str(is_student))

# Modern f-string approach (cleaner and auto-converts types)
print(f"Student Name: {name} is {age} years old student status: {is_student}")

# f-strings can evaluate arbitrary expressions directly inside {}
print(f"2 + 3 = {2 + 3}")  # "2 + 3 = 5"
```

---

## Splitting & Repetition

```python
# Splitting strings into lists by delimiter
stamp = "2026-10-28 20:44"
parts = stamp.split(" ")
print(parts)  # ['2026-10-28', '20:44']

# String repetition using the * operator
print("ha" * 3)  # "hahaha"
```

---

## Indexing & Slicing

Python supports both zero-based positive indexing and negative indexing from the end:

- **Positive Indices**: `0` to `len - 1` (left to right)
- **Negative Indices**: `-1` to `-len` (right to left)
- **Syntax**: `string[start:end:step]` (the `end` index is **excluded**)

```text
 Index:   0   1   2   3   4   5
 Char:    P   y   t   h   o   n
Neg Idx: -6  -5  -4  -3  -2  -1
```

```python
text = "Python"

# Direct index
print(text[1])  # 'y'

# Slicing from negative index -5 ('y') up to -2 ('o' excluded)
print(text[-5:-2])  # 'yth'

# Slicing with step: string[start:end:step]
word = "hello"
print(word[::2])  # 'hlo' (every 2nd character)
```

---

## Whitespace & Character Stripping

Use strip methods to trim whitespace or unwanted characters from string boundaries:

```python
word = " tree "

# Removes leading whitespace
print(repr(word.lstrip()))  # 'tree '

# Removes trailing whitespace
print(repr(word.rstrip()))  # ' tree'

# Removes both leading and trailing whitespace
print(repr(word.strip()))   # 'tree'

# In-between spaces are preserved!
job = "data engineer"
print(job.strip())  # "data engineer"

# Stripping custom characters from edges
tag = "###tree###"
print(tag.strip("#"))  # "tree"
```

---

## Case Conversion

```python
text = "PYTHON programming"

print(text.lower())  # "python programming"
print(text.upper())  # "PYTHON PROGRAMMING"

# Method chaining: convert case and trim whitespace
clean = text.lower().strip()
```

---

## Searching & Validation

### 1. Substring Search & Inspection

```python
phone = "+91-1234567890"

# .find() returns the first index or -1 if not found
print(phone.find("-"))          # 3

# Prefix and Suffix checks
print(phone.startswith("+91"))  # True
print(phone.endswith("90"))     # True

# Membership test with 'in' operator
email = "knight@gmail.com"
print("@" in email)             # True
```

### 2. Character Classification

```python
country = "USA"

print(country.isalpha())    # True  (all alphabetic characters)
print(country.isnumeric())  # False (contains letters, not numeric digits)
```

---

## Quick Reference Summary

| Method | Description | Return Value / Example |
| :--- | :--- | :--- |
| `s.count(sub)` | Counts occurrences of substring | `int` |
| `s.replace(a, b)` | Replaces occurrences of `a` with `b` | New `str` |
| `s.split(sep)` | Splits string into list on delimiter | `list[str]` |
| `s[start:end:step]` | Sequence slice (end exclusive) | Substring |
| `s.strip([chars])` | Removes edge whitespace / characters | New `str` |
| `s.lower() / s.upper()` | Converts character case | New `str` |
| `s.find(sub)` | Finds index of first match (or `-1`) | `int` |
| `s.startswith(prefix)` | Checks if string begins with prefix | `bool` |
| `s.endswith(suffix)` | Checks if string ends with suffix | `bool` |
| `s.isalpha()` | Checks if all characters are letters | `bool` |
| `s.isnumeric()` | Checks if all characters are digits | `bool` |
