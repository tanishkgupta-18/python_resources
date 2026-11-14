# Conditional Statements

Control flow decisions in Python are driven by `if`, `elif`, and `else` blocks, concise ternary inline expressions, and modern structural pattern matching (`match...case`).

---

## Standard Branching: `if`, `elif`, `else`

Python uses indentation (typically 4 spaces) rather than curly braces `{}` to define code blocks:

```python
score = 100

if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
else:
    print("Grade: F")
```

**Expected Output:**
```text
Grade: A
```

---

## Inline Ternary Expressions

Python allows single-line conditional expressions (ternary operators) to keep assignments concise.

### Syntax
```python
value_if_true if condition else value_if_false
```

### Examples

```python
score = 100

# Simple binary ternary assignment
status = "Pass" if score >= 50 else "Fail"
print(status)  # "Pass"

# Direct inline check
grade = "A" if score >= 90 else "F"
print(grade)   # "A"

# Chained ternary expression (use sparingly for readability)
result = "A" if score >= 90 else "B" if score >= 80 and score < 90 else "F"
print(result)  # "A"
```

::: tip Code Readability
While chained inline conditionals are syntactically valid in Python, prefer standard `if-elif-else` blocks for complex multibranch logic to maintain clean, readable code.
:::

---

## Structural Pattern Matching (`match...case`)

Introduced in **Python 3.10**, the `match...case` statement provides robust pattern matching. Multiple alternative patterns can be grouped using the pipe operator `|`:

```python
country = "India"

match country:
    case "United States" | "USA" | "US":
        print("US")
    case "India":
        print("IN")
    case "Japan":
        print("JP")
    case "United Kingdom" | "UK":
        print("UK")
    case _:
        print("Unknown Country")  # Default fallback wildcard
```

**Expected Output:**
```text
IN
```

### Key Advantages of Pattern Matching
- **Multiple Matches in One Line**: The `|` character acts as an OR operator across distinct case literals.
- **Wildcard Default**: The `case _:` branch acts as an exhaustive catch-all pattern (similar to `default:` in C/Java).
- **Expressive Guard Conditions**: Can match literal values, sequences, or object structures.

---

## Quick Reference Summary

| Construct | Syntax Pattern | When to Use |
| :--- | :--- | :--- |
| Standard `if` Block | `if cond: ... elif: ... else: ...` | Standard multi-line logic and branches |
| Ternary Operator | `val1 if cond else val2` | Direct single-line value assignments |
| Pattern Matching | `match val: case a \| b: ...` | Clean mapping of values or structured variants |
