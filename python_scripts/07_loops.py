# for i(loop variable) in (1,2,3...)sequence
# python takes this (1,2,3...) sequence and create object called iterator
# an iterator(object) that let you go through items one by one in a sequence

for i in (1,2,3,4,5):
    print(i)

# range(stop) => 0, 1, 2, 3 ... stop-1
for i in range(5):
    print(i)

# range(start, stop) => start...stop-1
for i in range(1, 5):
    print(i)

# range(start, stop, step) => i += step
print(10*"=")

for i in range(1, 10, 2):
    print(i)

# break and continue also used with loops

# another one is pass it is a placeholder where nothing happens

# else in for loop

for i in range(5):
    print(i)
else:
    print("finished")

# WHILE LOOP

i = 0
while i < 4:
    print(i)
    i += 1 
