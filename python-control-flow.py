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