# Boolean Expression

# True and False

# bool(value) -> boolean (True for non empty or non zero and False vice versa)

print(bool(123))

# in python we can do chained comparison

print(1 < 2 < 4)

age = 18

print(18 <= age <= 30)

# logical operations
print(age >= 18 and age <= 30)

print(age <= 18 or age >= 30)

print(not age == 18)

# and has more priority as compared to or but you can use () to evaluate or first

# in operator checks if value inside another value

print("a" in "Data") # return True
print("a" not in "Data") # return false

# is identity operator checks if two variables refer to the same object in memory

# var id data
# a -> 30 [1,2,4]
# b -> 40 [1,2,4]

a = [1,2,4]
b = [1,2,4]

# a is b check whether they points to same id or not
print(a is b) # returns false

# now a = b

a = b

print(a is b) # returns true

a == b # compares only the value

# But if value is simple the two different ids are not assigned

# for example

a = 5 
b = 5
print(a is b) # returns true since both points to same id

# None vs ""

# None means no value or unknown but "" means empty but it is known it is string

# when you are checking 'None' use 'is' instead of '=='

email = None
print(email is None)
