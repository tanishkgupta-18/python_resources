myDict = {"name": "John", "age": 30, "city": "New York"}

# dictionary are ordered, changeable, and do not allow duplicates keys.
# keys must be unique and of an immutable data type (string, number, tuple), while values can be of any data type and can be duplicated.

print(myDict)

user = {"id": 1, "name": "Alice", "age": 25, "city": "Los Angeles"}

# get the value of a specific key
print(user["name"])  # Output: Alice *raise KeyError if key does not exist

# .get() method to retrieve the value of a key
print(user.get("age"))  # Output: 25 *gives none if key does not exist

print(user.get("country", "Not Found"))  # Output: Not Found *gives default value if key does not exist

# check if a key exists in the dictionary

if "city" in user:
    print("City exists in the dictionary")  # Output: City exists in the dictionary

# we use in operator to check if a key exists in the dictionary. If the key is present, it returns True; otherwise, it returns False.

# View Objects in Dictionary
print(user.keys())  # Output: dict_keys(['id', 'name', 'age','city'])
print(user.values())  # Output: dict_values([1, 'Alice', 25, 'Los Angeles'])
print(user.items())  # Output: dict_items([('id', 1), ('name', 'Alice'), ('age', 25), ('city', 'Los Angeles')])

# Looping

for u in user:
    print(u, user[u])  # Output: id 1, name Alice, age 25, city Los Angeles

for key, value in user.items():
    print(key, value)  # Output: id 1, name Alice, age 25, city Los Angeles

# Add, Remove, and Update Items in Dictionary

user["email"] = "alice@example.com"
print(user)  

user.update({"age": 26, "city": "San Francisco"})
print(user)  # Output: {'id': 1, 'name': 'Alice', 'age': 26, 'city': 'San Francisco', 'email': 'alice@example.com'}

user.pop("email")
print(user)  # Output: {'id': 1, 'name': 'Alice', 'age': 26, 'city': 'San Francisco'}

user.pop("country", None)  # Does not raise an error if key does not exist
print(user)  # Output: {'id': 1, 'name': 'Alice', 'age': 26, 'city': 'San Francisco'}

user.pop("country", "Not Found")  # Returns default value if key does not exist
print(user)  # Output: {'id': 1, 'name': 'Alice', 'age': 26, 'city': 'San Francisco'}


user.popitem()  # Removes and returns the last inserted key-value pair
print(user)  # Output: {'id': 1, 'name': 'Alice', 'age': 26}

# creation

user = dict.fromkeys(["id", "name", "age"], None)

print(user)  # Output: {'id': None, 'name': None, 'age': None}

