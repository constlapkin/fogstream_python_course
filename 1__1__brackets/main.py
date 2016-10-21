# task 1
# brackets

s = input("Task 1 | enter string: ")
i = 0
q1 = 0
q2 = 0
q3 = 0
w = 0
for i in s:
    if i == "[":
        q1 += 1
    elif i == "{":
        q2 += 1
    elif i == "(":
        q3 += 1
    if i == "]":
        q1 -= 1
    elif i == "}":
        q2 -= 1
    elif i == ")":
        q3 -= 1
    else:
        w = 0
if q1 == 0 and q2 == 0 and q3 == 0:
    print ('yes')
else:
    print (-1)
