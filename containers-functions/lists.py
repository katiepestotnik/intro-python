# Lists equivalent to array in JS
# ordered list of elements

colors = ['red', 'green', 'blue', 'purple']
#list
#print(type(colors))
#print(len(colors))
#access individual with index
#print(colors[0])
# last item in list
#print(colors[len(colors)-1])

# access index programmtically with expression
#print(colors[2-1])

# use negative numbers to go backwards last item in list
#print(colors[-1])

# change item
colors[0]='yellow'
#print(colors)

#add item - only one item at a time to end
colors.append('black')
#print(colors)

# add multiple items with []
colors.extend(['indigo', 'lime green', 'electric yellow'])
#print(colors)

# add item in a specific spot - adds doesn't remove the original index value
colors.insert(1, 'red')
#print(colors)

#remove last thing by default, or specify with index
colors.pop()
#print(colors)
#specific
colors.pop(2)
#print(colors)
# works with delete operator as well
del colors[0]
#print(colors)
# remove a specific value
colors.remove('blue')
#print(colors)

# remove everything 
colors.clear()
#print(colors)
# add some colors back in
colors.extend(['red', 'green', 'blue'])
#print(colors)

# interating over lists
for color in colors:
    print(color)
    
# interating to get index
# all classes
#print(dir(enumerate(colors)))

for idx, color in enumerate(colors):
    print(idx, color)
    

