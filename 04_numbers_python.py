import math
import random
# Casting

x = 3.14
int(x)
y = 3
float(y)

p = 3, q = 4
complex(p, q)

# Operators

# in python if you do x / y you get float division and x // y is floor division
# 7 / 2 = 3.5(float) and 7 / 2 = 3(int)

# 2 ** 3 for exponentiation 2x2x2

# built in maths

x = -3
abs(x)

price = 35.34567
round(price, 3) 
# if ties 1.5 etc go to the nearest even no. which is 2 in this case
math.ceil(price)
math.floor(price)

# it removes the decimal part and return integer part
math.trunc(price)

print(random.random()) # floating random no. [0.0, 1.0]

print(random.randint(1, 6)) # random int value btw 1 and 6

x = 7.0

x.is_integer() # returns true since no decimal part

y = 7.1

y.is_integer() # returns false

isinstance(x, int) # returns false since x is float
