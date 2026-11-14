# Loops & Iteration

Loops allow executing a block of statements repeatedly. In Python, iteration centers on the **iterator protocol**, flexible `range()` sequence generation, control flow directives (`break`, `continue`, `pass`), the unique `else` clause, and `while` loops.

---

## The `for` Loop & Iterators

In Python, a `for` loop does not merely increment a counter; it iterates over an **iterable** (a sequence or collection) by creating an **iterator** object under the hood:

```python
# Iterating directly through a sequence of values
for i in (1, 2, 3, 4, 5):
    print(i)
```

**Expected Output:**
```text
1
2
3
4
5
```

---

## Generating Number Sequences with `range()`

The built-in `range()` function generates an immutable sequence of numbers on demand with low memory overhead.

### 1. Single Argument: `range(stop)`
Generates numbers from `0` up to `stop - 1`:

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### 2. Two Arguments: `range(start, stop)`
Generates numbers from `start` up to `stop - 1`:

```python
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4
```

### 3. Three Arguments: `range(start, stop, step)`
Increments by `step` on each iteration:

```python
# Prints odd numbers between 1 and 9
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

---

## Loop Control Statements: `break`, `continue`, `pass`

Python provides three keywords for fine-grained loop control:

```python
# 'break' terminates the loop immediately
for n in range(10):
    if n == 5:
        break
    print(n)  # Prints 0, 1, 2, 3, 4

# 'continue' skips the remainder of the current iteration
for n in range(5):
    if n == 2:
        continue
    print(n)  # Prints 0, 1, 3, 4 (2 is skipped)

# 'pass' acts as a syntactical placeholder where no operation occurs
for n in range(3):
    if n == 1:
        pass  # TODO: implement logic later
    print(n)
```

---

## The `for...else` Construct

Python uniquely supports an `else` block attached directly to loops. The `else` block executes **only if the loop terminates normally** (without encountering a `break` statement):

```python
for i in range(5):
    print(i)
else:
    print("finished")
```

**Expected Output:**
```text
0
1
2
3
4
finished
```

::: tip Practical Use of `for...else`
The `for...else` pattern is ideal for search operations:
```python
target = 10
items = [1, 3, 5, 7]

for num in items:
    if num == target:
        print("Found target!")
        break
else:
    print("Target not found in items.") # Executes only if loop completes without break
```
:::

---

## The `while` Loop

A `while` loop continues executing as long as its condition remains `True`:

```python
i = 0
while i < 4:
    print(i)
    i += 1
```

**Expected Output:**
```text
0
1
2
3
```

::: warning Guard Against Infinite Loops
Always ensure the loop condition is updated inside the `while` block (e.g. `i += 1`), otherwise the loop will run indefinitely until interrupted.
:::

---

## Summary Reference

| Construct | Purpose | Example |
| :--- | :--- | :--- |
| `for item in seq` | Iterates over elements of an iterable | `for x in [1, 2]:` |
| `range(stop)` | Range from `0` to `stop - 1` | `range(5) -> 0..4` |
| `range(start, stop, step)` | Range with start offset and step interval | `range(0, 10, 2)` |
| `break` | Immediately exits loop | `if cond: break` |
| `continue` | Skips to next iteration | `if cond: continue` |
| `pass` | Null statement placeholder | `def todo(): pass` |
| `for ... else` | Executes when loop completes without `break` | `else: print("Done")` |
| `while condition:` | Runs while condition evaluates to `True` | `while count < 5:` |
