new_tuple = (1, 2, 3, 4, 5)
print(new_tuple)
print(new_tuple[0])  # Accessing the first element
print(new_tuple[-1])  # Accessing the last element

# we cannot update or change the elements of a tuple since they are immutable

# tuples are ordered, indexed, allow duplicates but not mutable.

my_set = {1, 2, 3, 4, 5}
print(my_set)

# set is unique, unordered, and mutable. It does not allow duplicates.

# ======================================================================

# Set Methods
# add() - Adds an element to the set

my_set.add(6)
print(my_set)

# update() - Updates the set with elements from another set or iterable

my_set.update([7, 8, 9])
print(my_set)

# remove() - Removes an element from the set. Raises KeyError if the element is not found.
my_set.remove(3)
print(my_set)

# discard() - Removes an element from the set if it is present. Does not raise an error if the element is not found.
my_set.discard(10)  # Element 10 is not in the set, but no error will be raised
print(my_set)

# Maths Operations on Sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union - Returns a set containing all unique elements from both sets
union_set = set_a.union(set_b)

print("Union:", union_set)

# Intersection - Returns a set containing only the elements that are common to both sets
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference - Returns a set containing elements that are in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference:", difference_set)

# Symmetric Difference - Returns a set containing elements that are in either set_a or set_b but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_set)

# Relational Operators on Sets

# Subset - Checks if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)
print("Is set_a a subset of set_b?", is_subset)

# Superset - Checks if set_a is a superset of set_b
is_superset = set_a.issuperset(set_b)
print("Is set_a a superset of set_b?", is_superset)

# Disjoint - Checks if set_a and set_b have no elements in common
is_disjoint = set_a.isdisjoint(set_b)
print("Are set_a and set_b disjoint?", is_disjoint)



