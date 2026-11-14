# Python Essentials

Python essentials form the bedrock of the language: capturing user input, displaying formatted terminal output, using escape characters, handling multiline strings, and understanding variable assignments and the `None` type.

---

## Interactive User Input

The built-in `input()` function prompts the user for keyboard input and returns it as a **string** (`str`). Because `input()` always returns text, numerical inputs must be explicitly type-cast using functions like `int()` or `float()`.

```python
# Capturing text input
name = input("Enter your name: ")

# Capturing numerical input with type casting
age = int(input("Enter your age: "))

# Output using formatted string (f-string)
print(f"Hello {name}!")
print(f"You are {age} years old.")
```

::: tip Important Note on Input Persistence
The `input()` function captures user input but discards it immediately if it is not assigned to a variable:
```python
age = int(input("Enter the age:")) # Stored in 'age' for subsequent usage
print("Age is:", age)
```
:::

---

## Escape Characters & Multiline Strings

When printing text containing special symbols (like quotes or backslashes), Python uses the backslash `\` as an escape character.

### 1. Escaping Quotes and Backslashes

```python
# Escaping double quotes inside double-quoted strings
print("Hello! Welcome to the \"Python\" Basics program.")

# Escaping backslashes (e.g., Windows directory paths)
print("C:\\users\\newuser")
```

**Expected Output:**
```text
Hello! Welcome to the "Python" Basics program.
C:\users\newuser
```

### 2. Multiline Strings & Tab Indentation

Triple quotes (`"""` or `'''`) enable multiline strings preserving formatting, newlines, and escape sequences such as `\t` (tab character):

```python
print("""
Path:
\t -user
\t -newuser
""")
```

**Expected Output:**
```text
Path:
	 -user
	 -newuser
```

---

## Printing with Multiple Arguments

When multiple comma-separated arguments are passed into `print()`, Python automatically inserts a space between each argument:

```python
name = "Tanishk"

print("My name is", name)
print(name, "is a Software Engineer at Amazon") # Each comma adds a space
print("System Design, AI are the expertise of", name, "Currently Working at Amazon")
```

**Expected Output:**
```text
My name is Tanishk
Tanishk is a Software Engineer at Amazon
System Design, AI are the expertise of Tanishk Currently Working at Amazon
```

---

## The `None` Value

`None` is a special constant in Python representing the absence of a value, an uninitialized state, or "unknown/nothing".

```python
age = None  # None means unknown, empty, or unassigned

print(age)
print(type(age))
```

**Expected Output:**
```text
None
<class 'NoneType'>
```

::: info Key Takeaway
`None` is not equal to `0`, `False`, or an empty string `""`. It has its own distinct type: `NoneType`. In Python, `is None` is the standard and idiomatic way to test for null values.
:::

---

## Summary Reference

| Syntax / Construct | Behavior | Example |
| :--- | :--- | :--- |
| `input(prompt)` | Reads a line of user input as a string | `name = input("Name: ")` |
| `int(value)` | Converts value to integer | `age = int(input())` |
| `f"Hello {var}"` | Interpolates expressions inside strings | `f"Age: {age}"` |
| `\"`, `\\`, `\t`, `\n` | Escape sequences: quote, backslash, tab, newline | `print("Path:\\dir\tname")` |
| `""" ... """` | Multiline string literal | Triple-quoted block |
| `None` | Singleton object denoting "no value" | `result = None` |
