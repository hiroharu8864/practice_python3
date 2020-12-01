import math
import sys

import termcolor

num = 1
name = 'hirochan'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

print('Hi', 'Hirochan', sep=',', end='\n')
print('Hi', 'Hirochan', sep=',', end='\n')

result = math.sqrt(25)
print(result)
#print(help(math))

is_ok = [1, 2, 3, 4 ,5]
if is_ok:
    print('OK!')
else:
    print('Not OK!')

print(1 is 2)

count = 0
while count < 10:
    print(name)
    count += 1

contents = "Today is a very hot.Today is a very hot.Today is a very hot."
count_dict = {}
for c in contents:
    count_dict.setdefault(c, 0)
    count_dict[c] += 1
print(count_dict)

print(termcolor.colored('hello', 'green'))
print(termcolor.colored('hello', 'cyan'))
print(termcolor.__file__)
print(sys.path)
