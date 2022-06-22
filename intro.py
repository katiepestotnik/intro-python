# Python is an object oriented programming language 
# comment out code with #

"""
multiple lines
comment out with or '''
docstring means comment 
"""

# variables / case sensitive 
# naming convention snake casing
#
my_number = 15.5
print(my_number)
# you can reassign 
my_number = -4
print(my_number)

# check type of variable
print(type(my_number))

# int = whole number vs float = decimal
my_add = 4 + 5.5
print(my_add)

# complex numbers j is imaginery number
my_complex = 3+4j
print(type(my_complex))

# booleans
my_truth = True
my_false = False 
print(type(my_truth))

# None Type
no_value = None
print(type(no_value))

# Math Operators
'''
Addition (+)
Subtraction (-)
Multiplcation (*)
Division (/)
Modulo (remainder) (%)
Exponentiation (**)
'''

# get whole number instead of decimal, truncates 
quotient = 5//2
print(quotient)

# shortcut assignment operators
num = 10
num = num + 1
print(num)

num += 5
print(num)

num /= 2
# decimal
print(num)
#num //= 2
# no decimal
#print(num)

# Ternary
'''
Javascript
// Using the ternary operator/expression
let beverage = age >= 21 ? "Beer" : "Milk"

// Without a ternary expression
let beverage
if (age >= 21) {
  beverage = "Beer"
} else {
  beverage = "Milk"
}
'''
# PYTHON ternary 
age = 2
beverage = "beer" if age >= 21 else "water"
print(beverage)

# converting between data types
num_string = str(25)
print(type(num_string))
num_string = 25
print(type(num_string))

'''
str(item)        # Converts item to a string
int(item, base)  # Converts the provided item to an integer with the provided base
float(item)      # Converts the item to a floating-point number
hex(int)         # Converts an integer to a hexadecimal STRING
oct(int)         # Converts an integer to an octal STRING
tuple(item)      # Converts item to a tuple
list(item)       # Converts item to a list
dict(item)       # Converts item to a dictionary
'''

# string syntax
single_line = "hello world"
multi_line = '''
hello
world
'''
print(multi_line)

# concatenation 
one = 'one'
two = 'two'
both = one + two
print(both)

#interpolation with f-Strings
state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
print(message)


# string methods
# split
#'hello'.split('') # error
#python has to use list()
print(list("hello"))

# index
print('index'.index('n'))

# uppercase
print('big'.upper())

#lowercase
print('SMALLER'.lower())

# replace replaces all instances of the first argument 
print('hello friend friend'.replace('friend', 'kim'))

# contains returns boolean / substring
print("eggs" in "green eggs and ham")

# length of string => 9
# built in function 
print(len("Tacos yay"))
# breaks since built in function print("hello".len())

#bracket notation in sequences
intro = 'what is up'
print(intro[2])
print(intro[-1]) #last item in sequence