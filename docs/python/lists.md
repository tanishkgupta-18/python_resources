# Lists & Comprehensions

Lists (`list`) are ordered, mutable collections capable of storing heterogeneous data types. In Python, lists are implemented under the hood as dynamic arrays of pointers, offering `O(1)` random index access and rich manipulation methods.

---

## Creation & Memory Model

```python
# Empty lists
empty_literal = []
empty_constructor = list()

# Initialized lists
letters = ['a', 'b', 'c', 'd']
from_string = list('abcd')       # ['a', 'b', 'c', 'd']
from_range = list(range(5))       # [0, 1, 2, 3, 4]

# Heterogeneous elements
mixed = [1, 2.5, 'hello', True]

# Multidimensional lists (Matrices)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mixed_matrix = [[1, 2.5, 'hello'], [True, None, [1, 2]]]
```

::: info Memory Architecture
A Python list does not store values directly inside the contiguous memory block. Instead, it stores **pointers** referencing the actual objects elsewhere in heap memory.
:::

---

## Extended Unpacking (`*` and `_`)

Python allows extracting elements into variables using sequence unpacking:

```python
person = ['John', 'Doe', 30]

# Standard exact unpacking
name, surname, age = person

# Gathering middle elements with the * rest operator
name, *details, age = person
print(details)  # ['Doe']

# Discarding values with the _ throwaway placeholder
name, _, age = person

# Combining * and _ to discard multiple intermediate values
name, *_, age = person
```

---

## Built-in Aggregations & Inspection

Python provides top-level aggregation functions that work seamlessly across lists:

```python
nums = [1, 2, 3, 4, 5]

print(all(nums))  # True  (all items are truthy / non-zero)
print(any(nums))  # True  (at least one item is truthy)
print(max(nums))  # 5
print(min(nums))  # 1
print(sum(nums))  # 15

# Counting and finding indices
print(nums.count(3))  # 1 (frequency of element 3)
print(nums.index(3))  # 2 (first index position where 3 occurs)
```

---

## Mutations: Adding & Removing Elements

```python
nums = [1, 2, 3, 4, 5]

# append(val): appends to the end of the list in O(1) time
nums.append(6)

# insert(index, val): inserts element at given index
nums.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]

# remove(val): removes the first occurrence of the specified value
nums.remove(3)     # [0, 1, 2, 4, 5, 6]

# pop([index]): removes and returns item (defaults to last element)
last_item = nums.pop()    # Removes and returns 6
first_item = nums.pop(0)  # Removes and returns 0

# clear(): empties the entire list
# nums.clear()
```

---

## Sorting & Reversing: In-place vs New List

Understanding whether an operation modifies in-place or produces a new container is vital:

```python
letters = ['d', 'b', 'a', 'c']

# 1. In-place sort (modifies original list, returns None)
letters.sort()
print(letters)  # ['a', 'b', 'c', 'd']

letters.sort(reverse=True)
print(letters)  # ['d', 'c', 'b', 'a']

# 2. Built-in sorted() (leaves original intact, returns new list)
original = ['z', 'x', 'y']
new_sorted = sorted(original)
print(original)    # ['z', 'x', 'y'] (unchanged)
print(new_sorted)  # ['x', 'y', 'z']

# 3. Reversing
letters.reverse()                         # In-place reversal
new_reversed = list(reversed(letters))    # Generates a new reversed list
```

---

## Copying: References, Shallow Copy & Deep Copy

```python
# 1. Reference assignment (same memory pointer)
original = [1, 2, 3]
copy_ref = original
copy_ref.append(4)
print(original)  # [1, 2, 3, 4] -> Both changed!

# 2. Shallow Copy (.copy())
real_copy = original.copy()
real_copy.append(5)
print(original)   # [1, 2, 3, 4] -> Original unchanged
print(real_copy)  # [1, 2, 3, 4, 5]

# 3. Shallow Copy with Nested Containers Caveat
matrix = [[1, 2], [3, 4]]
shallow_matrix = matrix.copy()
shallow_matrix[0][0] = 999
print(matrix[0][0])  # 999 -> Inner lists were shared!

# 4. Deep Copy via 'copy.deepcopy'
import copy
clean_matrix = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(clean_matrix)
deep_copy[0][0] = 888

print(clean_matrix[0][0])  # 1 (remains completely isolated)
print(deep_copy is clean_matrix)  # False
```

---

## Combining Lists: Concatenation, Extend & Zip

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + creates a brand new list
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Using .extend() mutates list1 in-place
list1.extend(list2)       # list1 is now [1, 2, 3, 4, 5, 6]

# zip pairs corresponding elements up to the shortest sequence length
pairs = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(pairs)  # [('a', 1), ('b', 2), ('c', 3)]
```

---

## Iterators, `enumerate()`, and Functional Tools

```python
names = ['John', 'Doe', 'Jane', 'Smith']

# iter() and next()
stream = iter(names)
print(next(stream))  # "John"
print(next(stream))  # "Doe"

# enumerate(): attaches zero-based index (or custom start)
letters = ['a', 'b', 'c', 'd']
print(list(enumerate(letters, start=1)))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

for idx, val in enumerate(letters):
    print(idx, val)

# map(): transforms each element
nums_str = ['1', '2', '3', '4']
nums_int = list(map(int, nums_str))  # [1, 2, 3, 4]

# filter(): filters out falsy elements
dirty = ['a', '', None, False, 'b']
clean = list(filter(None, dirty))   # ['a', 'b']
```

---

## Lambda Functions & List Comprehensions

### Lambda Functions
Anonymous, single-expression functions:

```python
square = lambda x: x ** 2
add = lambda x, y: x + y

print(square(5))    # 25
print(add(5, 10))   # 15

# Lambdas with map and filter
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4]))   # [1, 4, 9, 16]
evens = list(filter(lambda x: x > 2, [1, 2, 3, 4]))    # [3, 4]
```

### List Comprehensions
List comprehensions provide a concise, readable, and faster alternative to traditional loops or `map/filter`:

::: tip Syntax Structure
```python
[expression for item in iterable if condition]
```
- **Expression**: Output value or transformation applied to each item.
- **Iteration**: Standard `for item in iterable` sequence traversal.
- **Filtering (Optional)**: `if condition` predicate to include or omit items.
:::

```python
# 1. Transformation
squares = [x ** 2 for x in [1, 2, 3, 4]]
print(squares)  # [1, 4, 9, 16]

# 2. Transformation with Filtering
prices = [100, 200, 300, 400, 500]
discounted = [price * 0.9 for price in prices if price > 200]
print(discounted)  # [270.0, 360.0, 450.0]

# 3. Simple Filtering
filtered_prices = [price for price in prices if price > 200]
print(filtered_prices)  # [300, 400, 500]
```

---

## Summary Reference

| Operation | Syntax | Complexity / Behavior |
| :--- | :--- | :--- |
| Append | `lst.append(x)` | `O(1)` amortized |
| Pop last | `lst.pop()` | `O(1)` |
| Pop index | `lst.pop(i)` | `O(n)` |
| In-place Sort | `lst.sort()` | `O(n log n)` via Timsort |
| Copy | `lst.copy()` | Shallow copy |
| Deep Copy | `copy.deepcopy(lst)` | Recursive deep copy |
| Comprehension | `[f(x) for x in lst if cond]` | Idiomatic sequence construction |
