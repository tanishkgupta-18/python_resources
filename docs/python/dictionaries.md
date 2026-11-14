# Dictionaries

Dictionaries (`dict`) are associative mappings storing data in **key-value pairs**. Under the hood, Python dictionaries are implemented via highly optimized hash tables, guaranteeing `O(1)` average time complexity for lookups, insertions, and deletions.

---

## Dictionary Properties & Key Rules

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
```

### Core Characteristics
1. **Ordered**: Preserves item insertion order (guaranteed since Python 3.7+).
2. **Mutable**: Values can be updated, keys added, and pairs removed dynamically.
3. **No Duplicate Keys**: Assigning to an existing key replaces its value.
4. **Key Immutability**: Keys **must** be hashable and immutable (e.g. `str`, `int`, `float`, `tuple`). Mutable objects like `list` or `dict` cannot be keys!
5. **Arbitrary Values**: Values can be of any data type, nested, or duplicated.

---

## Accessing Values: Direct `[]` vs Safe `.get()`

```python
user = {"id": 1, "name": "Alice", "age": 25, "city": "Los Angeles"}

# 1. Direct index access (raises KeyError if key does not exist)
print(user["name"])  # "Alice"

# 2. Safe retrieval with .get() (returns None by default if key is absent)
print(user.get("age"))      # 25
print(user.get("country"))  # None (no exception raised!)

# 3. Providing a custom default fallback with .get()
print(user.get("country", "Not Found"))  # "Not Found"
```

::: tip KeyError Prevention
Always prefer `dict.get(key, fallback)` over direct indexing `dict[key]` when dealing with dynamic external inputs, API responses, or optional configuration keys.
:::

---

## Membership Testing with `in`

The `in` operator checks whether a key exists in the dictionary in `O(1)` time:

```python
user = {"id": 1, "name": "Alice", "age": 25, "city": "Los Angeles"}

if "city" in user:
    print("City exists in the dictionary")
```

::: info Lookups Test Keys, Not Values
By default, `"Alice" in user` evaluates to `False`. To check values, explicitly query `user.values()`:
```python
print("Alice" in user.values())  # True (runs in O(n) linear scan)
```
:::

---

## Dynamic View Objects: `keys()`, `values()`, `items()`

Dictionary views provide dynamic windows into the dictionary's contents without allocating new lists:

```python
user = {"id": 1, "name": "Alice", "age": 25, "city": "Los Angeles"}

print(user.keys())
# dict_keys(['id', 'name', 'age', 'city'])

print(user.values())
# dict_values([1, 'Alice', 25, 'Los Angeles'])

print(user.items())
# dict_items([('id', 1), ('name', 'Alice'), ('age', 25), ('city', 'Los Angeles')])
```

---

## Iterating Over Dictionaries

```python
user = {"id": 1, "name": "Alice", "age": 25, "city": "Los Angeles"}

# Iterating over keys directly
for key in user:
    print(key, "->", user[key])

# Idiomatic unpacking of key-value pairs using .items()
for key, value in user.items():
    print(f"{key}: {value}")
```

**Expected Output:**
```text
id: 1
name: Alice
age: 25
city: Los Angeles
```

---

## Mutations: Adding, Updating & Deleting

```python
user = {"id": 1, "name": "Alice", "age": 25, "city": "Los Angeles"}

# 1. Adding a new key-value pair
user["email"] = "alice@example.com"

# 2. Updating multiple entries at once using .update()
user.update({"age": 26, "city": "San Francisco"})
print(user)
# {'id': 1, 'name': 'Alice', 'age': 26, 'city': 'San Francisco', 'email': 'alice@example.com'}

# 3. Removing by key with .pop()
removed_email = user.pop("email")  # Returns removed value

# 4. Safe popping with fallback (avoids KeyError if key missing)
user.pop("country", None)          # Returns None safely
user.pop("country", "Not Found")   # Returns "Not Found" safely

# 5. .popitem() removes and returns the LAST inserted (key, value) pair
last_pair = user.popitem()
print(last_pair)  # ('city', 'San Francisco')
```

---

## Initializing with `dict.fromkeys()`

Quickly generate a dictionary initialized with a default template value across multiple keys:

```python
keys = ["id", "name", "age"]

user_template = dict.fromkeys(keys, None)
print(user_template)
```

**Expected Output:**
```text
{'id': None, 'name': None, 'age': None}
```

::: warning Mutable Defaults in fromkeys()
If you provide a mutable object like `[]` as the default value in `dict.fromkeys(keys, [])`, all keys will share the **same reference**. Always use comprehensions for mutable defaults:
```python
user_lists = {k: [] for k in keys}
```
:::

---

## Summary Reference

| Method / Syntax | Description | Time Complexity |
| :--- | :--- | :--- |
| `d[key]` | Direct lookup (throws `KeyError` if missing) | `O(1)` avg |
| `d.get(key, default)` | Safe retrieval with fallback | `O(1)` avg |
| `key in d` | Membership check against keys | `O(1)` avg |
| `d.update({...})` | Merges keys and values into `d` | `O(k)` where `k` is size |
| `d.pop(key[, def])` | Removes key and returns value | `O(1)` avg |
| `d.popitem()` | Removes and returns last inserted `(k, v)` | `O(1)` |
| `d.keys() / d.values()` | Dynamic views of keys or values | `O(1)` |
| `d.items()` | Dynamic view of `(key, value)` tuples | `O(1)` |
| `dict.fromkeys(seq, val)`| Creates dictionary with identical initial values | `O(n)` |
