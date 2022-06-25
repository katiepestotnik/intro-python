# dictionaries 
# key/value pairs like an object in js
# JS object 
# const student = {
#     name: 'Katie',
#     course: 'SEIR'
# }
# python just needs quotes on the key can use other types as a key since it isn't always a string
# unordered and mutable 
student = {
    'name': 'Katie',
    'course': 'SEIR',
    'week': 18
}
print(type(student))
# access key
# square brackets - error if key doesn't exist (key error)
print(student["name"])
# .get second argument if key doesn't exist what should it be - None is a good argument(default) if it doesn't exist 
print(student.get('hello', None))
print(student.get('email', 'katie@gmail.com'))
#only gets doesn't set student remains the same
print(student)

# change value of key
student['name'] = 'Katie Pestotnik'
# add key and value
student['email'] = 'katie.pestotnik@gmail.com'
print(student)

# dictionary in operator
if 'course' in student:
    print(f"Student's name: {student['name']}")
else:
    print('Student has no name')

# delete key/value
del student['email']
print(student)

# find number of keys to dictionary
print(len(student))

# loop over the keys (any name doesn't have to be key)
for key in student:
    print(key, student[key])

# find key and value
print(student.items())
# same as line 45 lopping over list/tuples
for key, val in student.items():
    print(key, val)

where_my_things_arecontainer = {
    "Missy": "on my bed",
    "Klondike": "on the floor",
    "My Computer": "on my desk",
    "My Car": "in front of my house"
}
for key, value in where_my_things_arecontainer.items():
    print(f'{key} is kept {value}.')
    


