# Types
age = 24
print(type(str(age)))
#str(value) built-in function converts any value to a string.
print("My age is " + str(age) + " years old.") 

# Math
password = "123a"

# len(value) built-in function returns number of character in a string or number of items in a value
# it counts spaces as well if present in string
print(len(password))

# count(substring)
# is a method that returns the freq of substring in the give string

text = "My name is Name your name is name"
print(text.count("name")) # python is case sensitive therefore name appears 3 times

# String Based

# replace(current, to)

num = "123,23"
print(num.replace(",","."))

phone = "199-234-4566"
print(phone.replace("-", ""))

price = "$123-23-67"
print(price.replace("$", "").replace("-", ","))

# Transformation
folder = "C:\\users\\project\\"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)

# f-string
# A modern way to format and build strings f means formatted enable us to put variable and expression directly inside string value

name = "Tanishk"
age = 24
is_student = True

# old way
print("Student Name: " + str(name) + " is " + str(age) + " years old " + "student status: " + str(is_student))
# new way
print(f"Student Name: {name} is {age} years old student status: {is_student}") # here it automatically converts it to string.
print(f"2+3={2+3}") # expression

# split
stamp = "2026-10-28 20:44"
print(stamp.split(" ")) # it returns list of string with separation

print("ha"*3) # 3 times => hahaha

# indexing and slicing

# positive index starts from 0 to length - 1 and negative index starts from right side -1 goes to left with -length
# start:end where end is excluded and if you want upto the end just start:
# 0 1 2 3 4 and -5 -4 -3 -2 -1 

# [start:end:step] every stepth character will be leaved
# hello => step = 2 => hlo every 2th step is leave by default 1 so every char is display nothing leaved

text = "Python"

print(text[1])
print(text[-5:-2])

# strip

# lstrip() removes leading spaces and rstrip() removes trailing spaces and strip() removes both leading and trailing spaces

word = " tree "
word.lstrip()
print(word)
word.rstrip()
print(word)

word.strip()

word = "data engineer"
word.strip() # in between space is not removed only trailing and leading space only

word = "###tree###"
# we can remove # from both side
word.strip("#")

# Case Conversion
text = "PYTHON programming"

print(text.lower())
print(text.upper())

text.lower().strip()

# SEARCH

phone = "+91-1234567890"
print(phone.find("-")) # return index position if present else -1 
print(phone.startswith("+91")) # returns true
print(phone.endswith("90"))

email = "knight@gmail.com"
print("@" in email)

# Validation

country = "USA"

print(country.isalpha())
print(country.isnumeric())
