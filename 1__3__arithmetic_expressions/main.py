# task 3
# arithmetic expressions
import re

str = input("Task 3 | enter string: \n")

plus = re.findall('\d+ \+ \d+', str)
minus = re.findall('\d+ \- \d+', str)
multiply = re.findall('\d+ \* \d+', str)
split = re.findall('\d+ \/ \d+', str)
result = plus + minus + multiply + split

i = 0
while i < len(plus):
    operands = re.split('\+', plus[i])
    plus[i] = float(operands[0]) + float(operands[1])
    i += 1

i = 0
while i < len(minus):
    operands = re.split('\-', minus[i])
    minus[i] = float(operands[0]) - float(operands[1])
    i += 1

i = 0
while i < len(multiply):
    operands = re.split('\*', multiply[i])
    multiply[i] = float(operands[0]) * float(operands[1])
    i += 1

i = 0
while i < len(split):
    operands = re.split('\/', split[i])
    split[i] = float(operands[0]) / float(operands[1])
    i += 1

i = 0
while i < len(result):
    result[i] = result[i] + ' = '
    i += 1

i = 0
j = 0
while i < len(plus) :
    str = []
    str.append(result[j])
    str.append(plus[i])
    print(str)
    i += 1
    j += 1

i = 0
while i < len(minus):
    str = []
    str.append(result[j])
    str.append(minus[i])
    print(str)
    i += 1
    j += 1

i = 0
while i < len(multiply):
    str = []
    str.append(result[j])
    str.append(multiply[i])
    print(str)
    i += 1
    j += 1

i = 0
while i < len(split):
    str = []
    str.append(result[j])
    str.append(split[i])
    print(str)
    i += 1
    j += 1
