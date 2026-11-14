# Lists
empty = []
print(empty)
print(type(empty))

# List with values
letters = ['a', 'b', 'c', 'd']
print(letters)

# python creates a list object and store values in it also it creates an array of pointers to the values in the list object

# object
# list pointer -> 'a'

# mixed data types
mixed = [1, 2.5, 'hello', True]

# Create list
empty = list()

letters = list('abcd')

numbers = list(range(5))

# matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mixed_matrix = [[1, 2.5, 'hello'], [True, None, [1, 2]]]

# unpacking

person = ['John', 'Doe', 30]

name, surname, age = person

print(name)
print(surname)
print(age)

# if you dont want middle values you can use * to ignore them
name, *details, age = person

print(name)
print(details)
print(age)

# if you want to skip use _ as a placeholder
name, _, age = person
print(name)
print(age)

name, *_, age = person # Ignore the middle value

# using * and _ collectively to ignore multiple values

# all -> returns True if all values in the iterable are True
nums = [1, 2, 3, 4, 5]

print(all(nums)) # True
print(max(nums)) # 5
print(min(nums)) # 1
print(sum(nums)) # 15

# any -> returns True if any value in the iterable is True
print(any(nums)) # True

# count -> returns the number of occurrences of a value in the list

print(nums.count(3)) # 1

# index -> returns the index of the first occurrence of a value in the list
print(nums.index(3)) # 2

# append -> adds a value to the end of the list

nums.append(6)

# insert -> adds a value at a specific index in the list

nums.insert(0, 0) # adds 0 at index 0

# remove -> removes the first occurrence of a value in the list

nums.remove(3) # removes 3 from the list

# clear -> removes all values from the list

# nums.clear() # removes all values from the list

# .pop() -> removes and returns the value at a specific index in the list

nums.pop() # removes and returns the last value in the list

nums.pop(0) # removes and returns the value at index 0

# sorting lists

# sort -> sorts the list in place

letters = ['d', 'b', 'a', 'c']

letters.sort() # sorts the list in place
letters.sort(reverse=True) # sorts the list in place in reverse order
print(letters)

# sorted -> returns a new sorted list

newList = sorted(letters) # returns a new sorted list

# keeps the original list unchanged
print(newList)

letters.reverse() # reverses the list in place

newReverseList = list(reversed(letters)) # returns a new reversed list

# reversed(letters) returns an iterator that can be converted to a list using list()


# Copying lists

# shallow copy -> creates a new list object but the values in the list are references to the original values
original = [1, 2, 3]

copyList  = original # its a reference to the original list, not a copy

# above example is pointing to same list in memory, so if we change the original list, the copyList will also change vice versa

# Real Copy -> creates a new list object and copies the values from the original list to the new list

realCopyList = original.copy() # creates a new list object and copies the values from the original list to the new list

# matrix copy

# shallow copy of a matrix
matrix = [[1, 2], [3, 4]]

shallowCopy = matrix.copy() # creates a new list object but the sublists are references to the original sublists

# therefore if we change the original sublist, the shallowCopy will also change

# to solve this we can use deepcopy from the copy module

import copy

deepCopy = copy.deepcopy(matrix) # creates a new list object and copies the values from the original list to the new list

print(deepCopy is matrix) # False

# Combine Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# using + operator
combined = list1 + list2 # creates a new list object and copies the values from the original lists to the new list

# nested lists

nested = [list1, list2] # creates a new list object and copies the references to the original lists to the new list

# extend -> adds the values from one list to another list

list1.extend(list2) # adds the values from list2 to list1

# zip -> combines two lists into a list of tuples
zipped = list(zip(list1, list2)) # creates a list of tuples by combining corresponding elements from both lists

# but if len of lists are not equal, it will stop at the shortest list


# Iterators

# iterable -> an object that can be iterated over, like a list, tuple, set, dictionary, etc.
# iterator -> an object that represents a stream of data, it can be iterated over using the next() function

name = ['John', 'Doe', 'Jane', 'Smith']

iterator = iter(name)
print(next(iterator)) # John
print(next(iterator)) # Doe
print(next(iterator)) # Jane
print(next(iterator)) # Smith

# enumerate -> returns an iterator that produces pairs of index and value from the iterable

letters = ['a', 'b', 'c', 'd']

print(list(enumerate(letters))) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# why list is used with enumerate is because enumerate returns an iterator, and we need to convert it to a list to see the output

print(list(enumerate(letters, start=1))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

for index, value in enumerate(letters):
    print(index, value)

print(list(reversed(letters))) # ['d', 'c', 'b', 'a']

# reversed returns an iterator, and we need to convert it to a list to see the output

print(list(zip(letters, reversed(letters)))) # [('a', 'd'), ('b', 'c'), ('c', 'b'), ('d', 'a')]

# map(function, iterable) -> returns an iterator that applies the function to each value in the iterable

print(list(map(str.upper, letters))) # ['A', 'B', 'C', 'D']

numbers = ['1', '2', '3', '4']

print(list(map(int, numbers))) # [1, 2, 3, 4]

# filter(function, iterable) -> returns an iterator that filters the values in the iterable based on the function

letters = ['a', '', None, False, 'b', 'c', 'd']
print(list(filter(None, letters))) # ['a', 'b', 'c', 'd']

print(list(filter(bool, letters))) # ['a', 'b', 'c', 'd'] bool function returns True for non-empty values and False for empty values

# lambda function -> an anonymous function that can take any number of arguments, but can only have one expression

square = lambda x: x ** 2
print(square(5)) # 25

add = lambda x, y: x + y
print(add(5, 10)) # 15

# using lambda function with map and filter

print(list(map(lambda x: x ** 2, [1, 2, 3, 4]))) # [1, 4, 9, 16]
print(list(filter(lambda x: x > 2, [1, 2, 3, 4]))) # [3, 4]

# list comprehension -> a concise way to create lists

squares = [x ** 2 for x in [1, 2, 3, 4]]

# it comprises three parts: data transformation, iteration, and filtering. The data transformation is the expression that defines how to transform each element in the iterable. The iteration is the for loop that iterates over the iterable. The filtering is the optional if statement that filters the elements in the iterable.

prices = [100, 200, 300, 400, 500]

prices_with_discount = [price * 0.9 for price in prices if price > 200] # 10% discount

# how it works: for each price in prices, if the price is greater than 200, it applies the discount and adds it to the new list prices_with_discount

prices_cleaned = [price for price in prices if price > 200] # removes prices less than or equal to 200

