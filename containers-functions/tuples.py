# Tuples
# items are fixed cannot change, add, delete
# benefit more efficient for interpreter
# allows different types
colors = ('red', 'blue', 'green')
print(type(colors))
#length
print(len(colors))
# had to have trailing comma to be seen as tuple if only one item
red = ('red',)
print(type(red))

## withouth parenthesis still works
# defaults to tuple- least impact to memory
my_tuple = 'Red', 'Green', 'Blue'
print(type(my_tuple))

#accessing items
colors = ('red', 'green', 'blue')
green = colors[1]
print(green)
# index
blue_idx = colors.index('blue')
print(blue_idx)
#interating with enumerate
for idx, color in enumerate(colors):
    	print(idx, color)
# unpacking
katie = ('Katie', 39)
name, age = katie
print(name, age)

#Slice Operator
#assign a slice of sequence to variable
# starting index up to but not including second number
#can be list, tuple 
numbers = (1, 3, 4, 5)
some_nums = numbers[2:4]
print(some_nums)
copy = numbers[0:]
print(copy)