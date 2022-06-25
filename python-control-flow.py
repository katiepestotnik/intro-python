floor = 'sticky'
walls = 'clean'
walls = 'dusty'

if floor == 'sticky':
    print('Clean the floor')

if walls == 'sticky':
    print('Clean the walls')
elif walls == 'dusty':
    print('dust them')
else:
    print('nice clean walls')
    

#looping
#for
colors = ['green', 'yellow', 'red']
for color in colors:
    print(color)
#while
# while color != 'quit':
#     if color == 'green':
#         print('Go!!!')
#     elif color == 'yellow':
#         print('Slow Down')
#     elif color == 'red':
#         print('Stop or get a ticket')
#     elif color == 'quit':
#         print('user quit game')
#         break
#     else:
#         print('Not a traffic color light')
#     color = input('Enter "green", "yellow", "red": ').lower()
    
# ranges
for number in range(6):
    print(number)

for num in range(2, 10, 2):
    print(num)

#list
nums = list(range(10))
print(nums)
#tuple
tuples_nums = tuple(range(10))
print(tuples_nums)

#range negative step
for num in range(10, -5, -1):
    print(num)
