## Compiled vs Intrepeted

**Compiled** -  C++, Typescript, C#
finds errors before running code
1. source code
2. translated/compiler source code to machine code
3. run-time

**Intrepeted** - JS, Python, Ruby, PHP 
JS runs code line by line until it runs into error
1. source code
2. run-time: interpreter (node/python3) translate and executes

## Browser engines - chrome, microsoft edge, opera uses chrome V8 is a chromium JS interpreter 

## Typing - set of rules that applies "type" to data structures
- JS: primitives (boolean, num, string, symbol, null, undefined, bigint)
      nonprimitive (object/mapping, array/sequence)
- Python: primitives (integers, float, strings, boolean)
          nonprimitive (arrays/sequence, lists/sequence, tuples/sequence, dictionary/mapping, sets, files)

## Statically v Dynamically typed languages
- Statically: types checked before run-time
    Java, Typescript, C++ 
- Dynamically: types check during run-time
    JS, Python


## Truthy and Falsey
Falsey = False, None, Zero (0, 0.0 and 0j), '', [], (), {}, range(0)
 - JS [] and {} are truthy

Truthy = Everything else

## Comparison Operators
< less than
> greater than
<= less than or equal
>= greater than or equal
== equal to
!= not equal to

not is equavilant as bang 
    - not 0 == True

is operator will check ids
b = [1,2]
c = [1,2]
b == c // True values are the same
b is c // False ids are different, different locations in memory
b is not c // True

## Logical Operators 
Python == or JS === ||
Python == and JS === &&

or
If the first operand is truthy, return it, otherwise return the second operand.

and
If the first operand is falsey, return it, otherwise return the second operand.

True or False
# => True
False or True
# => True
'hello' or 0
# => 'hello'
0 or 'hello'
# => 'hello'
True and False
# => False
False and True
# => False
'hello' and 0
# => 0
0 and 'hello'
# => 0
'hello' and 'tacos'
# => 'tacos'