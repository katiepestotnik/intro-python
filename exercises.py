# Branching & Looping Exercises

color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')

# Write the if...elif...else statement as described in the lesson

if color == 'green':
    print('Go!!!')
elif color == 'yellow':
    print('Slow Down')
elif color == 'red':
    print('Stop or get a ticket')
else:
    print('Not a traffic color light')
