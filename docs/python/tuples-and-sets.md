# Tuples & Sets

Python features two distinct container types with fundamentally different guarantees: **Tuples** (ordered and immutable) and **Sets** (unordered, mutable, and strictly unique).

---

## Tuples: Ordered & Immutable Sequences

A **tuple** is an ordered collection of values enclosed in parentheses `()`. Unlike lists, tuples are **immutable**—once defined, their size and element bindings cannot be modified.

```python
new_tuple = (1, 2, 3, 4, 5)

print(new_tuple)
print(new_tuple[0])   # 1  (Accessing first element via index)
print(new_tuple[-1])  # 5  (Accessing last element via negative index)

# Attempting mutation raises an exception:
# new_tuple[0] = 99  # TypeError: 'tuple' object does not support item assignment
```

### Characteristics of Tuples
- **Ordered**: Retains precise insertion order.
- **Indexed**: Supports zero-based and negative indexing (`[0]`, `[-1]`).
- **Allows Duplicates**: Can store repeated identical elements.
- **Immutable**: Elements cannot be added, replaced, or deleted after creation.
- **Hashable**: A tuple containing only immutable elements can be used as a dictionary key or set element.

---

## Sets: Unordered & Unique Collections

A **set** is an unordered collection of unique, hashable objects enclosed in curly braces `{}`.

```python
# Duplicates are automatically eliminated
my_set = {1, 2, 3, 4, 5, 2, 3}
print(my_set)  # {1, 2, 3, 4, 5}
```

### Characteristics of Sets
- **Unique**: Discards any duplicate values automatically.
- **Unordered**: Elements have no stable index position (indexing like `my_set[0]` raises `TypeError`).
- **Mutable**: Elements can be dynamically inserted or removed.
- **Fast Lookups**: Membership testing (`x in my_set`) operates in `O(1)` average time complexity via hash table implementation.

---

## Set Mutations: `add`, `update`, `remove`, `discard`

```python
my_set = {1, 2, 3, 4, 5}

# add(elem): Adds a single element
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# update(iterable): Adds multiple elements from another collection
my_set.update([7, 8, 9])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove(elem): Removes element; RAISES KeyError if missing!
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5, 6, 7, 8, 9}

# discard(elem): Safely removes element; NEVER raises an error if missing!
my_set.discard(10)  # 10 is absent, but executes safely without error
```

::: tip remove() vs discard()
- Use `.remove()` when an absent element indicates a bug or invalid state that requires an error (`KeyError`).
- Use `.discard()` when you want idempotent deletion without throwing an exception.
:::

---

## Mathematical Set Operations

Sets support classical Venn diagram operations both through method calls and mathematical operator symbols:

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 1. Union (elements in set_a, set_b, or both)
union_set = set_a.union(set_b)  # or: set_a | set_b
print("Union:", union_set)
# Output: {1, 2, 3, 4, 5, 6}

# 2. Intersection (elements common to both sets)
intersection_set = set_a.intersection(set_b)  # or: set_a & set_b
print("Intersection:", intersection_set)
# Output: {3, 4}

# 3. Difference (elements in set_a but NOT in set_b)
difference_set = set_a.difference(set_b)  # or: set_a - set_b
print("Difference:", difference_set)
# Output: {1, 2}

# 4. Symmetric Difference (elements in either set, but NOT in both)
symmetric_diff = set_a.symmetric_difference(set_b)  # or: set_a ^ set_b
print("Symmetric Difference:", symmetric_diff)
# Output: {1, 2, 5, 6}
```

---

## Relational Operations on Sets

Test containment relationships between sets:

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Subset: Are all elements of set_a contained inside set_b?
print(set_a.issubset(set_b))    # False (or: set_a <= set_b)

# Superset: Does set_a contain all elements of set_b?
print(set_a.issuperset(set_b))  # False (or: set_a >= set_b)

# Disjoint: Do set_a and set_b share ZERO common elements?
print(set_a.isdisjoint(set_b))  # False (they share 3 and 4)

set_x = {1, 2}
set_y = {3, 4}
print(set_x.isdisjoint(set_y))  # True
```

---

## Comparing Tuples vs Sets vs Lists

| Feature | `list` | `tuple` | `set` |
| :--- | :--- | :--- | :--- |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| **Mutable?** | Yes | **No (Immutable)** | Yes |
| **Ordered?** | Yes | Yes | **No** |
| **Indexed?** | `lst[0]` | `tup[0]` | ❌ No |
| **Duplicates?** | Allowed | Allowed | **Disallowed (Unique)** |
| **Lookup Time** | `O(n)` | `O(n)` | **`O(1)` average** |
