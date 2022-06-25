# Functions

def add_nums(num1, num2):
    print(f'Num 1 = {num1}')
    print(f'Num 2 = {num2}')
    return num1 + num2
# can specify which parameter in the arguments
# key word/names arguments num1=10
print(add_nums(num2=3, num1=10))
print(add_nums(20, 10))
print(add_nums(22, 10))
print(add_nums(40, 10))

## args and kwargs *, **
# * all args = tuple can give as many args you want
# * dict of key word args
def get_all_args(*args, **kwargs):
    print(args[0:2])
    print(kwargs)
get_all_args(1, 2, 3, 4, cheese="cheddar", wine="red")

def add_all_nums(*args):
    count = 0
    for arg in args:
        count = count + arg
    return count
print(add_all_nums(1,2,3))

# defining empty functions
def first_function():
    pass
result = first_function()
print(result)

################
#Lambda
#python version of arrow - for callbacks
#lambda functions can only do one thing
add_numbers = lambda num1,num2: num1 + num2
print(add_numbers(2,5))

#python callback functions

##map(callback/lambda, array)
nums = [1, 2, 3, 4, 5, 6, 7]
#map(lambda, list)
map_result = (map(lambda num:num+1, nums))
map_result2 = tuple(map(lambda num:num+1, nums))
print(map_result2)
#returns map object can't see actual object
print(map_result)
# if you wrap the map with list() then it will return the new list
print(list(map_result))

# with list comprehension
result3 = [x+1 for x in nums]
print(result3)

# filter with python
# filter(lambda, list)
filter_result = filter(lambda num: num%2==0, nums)
print(list(filter_result))

#comprehesion
filter_comprehension = [num for num in nums if num%2==0]
print(filter_comprehension)

# do both edit numbers only if they are % 2 == 0
final = [num + 1 for num in nums if num%2==0]
print(final)