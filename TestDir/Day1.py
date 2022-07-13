"""
myGlobalVar = "Morning"
# My first Python Program

print("Welcome To Python")

# Python Variable

a = 5   # a is type of integer
z = "Python"   # z is type of string

myvar_1 = "Thrupthi"
_testVar = 10

print(a)
print(z)

print("Good"+" "+myGlobalVar)
"""
"""
#Data types in Python?

b = 5
print (type(b))

b = 5.2

print (type(b))

b = 1j

print (type(b))

b = ["Computer", "Keyboard", "Mouse"]

print (type(b))

b = ("Computer", "Keyboard", "Mouse")
print (type(b))

b = {"Name" : "Test", "Roll" : "11", "Class" : "V"}
print (type(b))
"""
"""
# Python Type Casting

a = int(5.2)
print (a)

x = float(10)
print (x)

b = str(3.0)
print (b)

"""
"""
# Python String Operations

#CUS-001
x = "Hello Python"
print(x[0])
print(x[1])

x = "Hello Python"
for a in x:
    print(a)

# Length of String

myAadharCardNumber = "1234567890"
print("My Aadhar Card digit length is:"+str(len(myAadharCardNumber)))

# Checking Partial String into a Complete text.

txt = "Training Solutions We Offer"
search_text = "Solutions"
print(search_text in txt)

"""
"""
# Python Operators

# Python Arithmetic Operators
print(10+10)
print(100-10)
print(10*10)
print(7 % 3)
print(8 % 3)
print(9 % 3)

# Python Assignment Operators

a = 1
a += 10  #a = a+10
"""
"""
x = 2
b = 2

# Python IF, ELSE

if x > 0 and x > 5:
    print("x is >0")

if x == b:
    print("x == b")

x = 55
y = 300

if y > x:
    print("Y is greater than X")

m = 4
n = 5

if m > n:
    print("m is greater than n")
elif m == n:
    print("m is equal to n")
else:
    print("Final String to print")

# One Liner if Statement

if n > m: print("n is greater than m")

CAT_Score = 98
GATE_Score = 96
My_Score = 97

if My_Score > GATE_Score or My_Score > CAT_Score:
    print("I can get an IIT")


# How To Use While Loop ??

a = 1

while a < 6:
    a += 1
    print(a)
    if a == 5:
        break

# For loop

cars = ["Toyota", "Honda", "Ford", "BMW", "GM", "Maruti"]

for a in cars:
    print(a)

for a in "Python":
    print(a)


cars = ["Toyota", "Honda", "Ford", "BMW", "GM", "Maruti"]

for a in cars:
    print(a)
    if a == "BMW":
        break

cars = ["Toyota", "Honda", "Ford", "BMW", "GM", "Maruti"]

for a in cars:
    print(a)
    if a == "BMW":
        continue
"""

"""
# range()?

for a in range(20):
    print(a)

for a in range(5 , 20):
    print(a)

for z in range(2, 30, 3):
    print(z)
"""
"""
# Python List

cars = ["Toyota", "Honda", "Ford", "BMW", "GM", "Maruti"]
print(cars)   # Print a list

# Print All items present in a List

for a in cars:
    print(a)

# Get List count

print(len(cars))

# List Type ???

print(type(cars))

# Getting single list item

print(cars[0])
print(cars[5])
"""

"""
# How to change Item present in a LIST?

cars = ["Toyota", "Honda", "Ford", "BMW", "GM", "Maruti"]
cars[1] = "KIA"
print(cars)

# How to change a range of Item Value ??

cars[0:2] = ["MG", "AUDI"]
print(cars)

# Adding into the List

cars.append("Eicher")
print(cars)

# Removing from the List

cars.remove("Eicher")
print(cars)
"""

"""
# Sorting a loop

rollnumber = [45, 33, 0, 5, 100, 22, 44]
rollnumber.sort()
print(rollnumber)

"""

"""
# PYTHON TUPLES

cars = ["Toyota", "Honda", "Ford", "BMW", "GM", "Maruti"]

# How to print a tuple ??

print(cars)
print(len(cars))   # how to print length of tuple

# How to change value of a tuple

mycars = list(cars)
mycars[2] = "BULLET"
cars = tuple(mycars)

print(cars)

# How to add an item in a tuple

mycars = list(cars)
mycars.append("Cycle")
cars = tuple(mycars)

print(cars)

# Looping  through a tuple

for x in cars:
    print(x)
    
"""
"""
# Python Dict

myCar = {
    "Name": "Thrupthi",
    "Place": "Mysore",
    "State": "Karnataka",
    "Country": "India",

}

# How to Print a Dict ?

print(myCar)


# How to Get a Dict ?

print(myCar["State"])
print(myCar["Name"])

"""
"""
# Duplicate Key is not allowed in Dict

myCar = {
    "Name": "Thrupthi",
    "Place": "Mysore",
    "State": "Karnataka",
    "Country": "India",
    "Country": "USA",

}

print(myCar)


# Duplicate length

myCar = {

    "Name": "Thrupthi",
    "Place": "Mysore",
    "State": "Karnataka",
    "Country": "India",

}

print(len(myCar))



# Add item in a Dict

myCar = {

    "Name": "Thrupthi",
    "Place": "Mysore",
    "State": "Karnataka",
    "Country": "India",

}

myCar["Company"] = "Arisglobal"

print(myCar)


# Remove item from a Dict

myCar.pop("Place")
print(myCar)


# Loop Keys in a Dict

for x in myCar:
    print(x)

# How to Get the Value in a Dict

for x in myCar:
    print(myCar[x])
"""
# Loop Keys and Values in Dic

myCar = {

    "Name": "Thrupthi",
    "Place": "Mysore",
    "State": "Karnataka",
    "Country": "India",

}

for x, y in myCar.items():
    print("If Key is"+x +" "+"Then Value is "+" "+y)