# task 4
# coordinates

import re

def min(list, max):
    min = max
    i = 0
    while i < len(list):
        j = 0
        l1 = re.split(' ', list[i])
        while j < len(list):
            if i != j:
                l2 = re.split(' ', list[j])
                x1 = l1[0]
                y1 = l1[1]
                x2 = l2[0]
                y2 = l2[1]
                if hypotenuse(x1, y1, x2, y2) < min:
                    min = hypotenuse(x1, y1, x2, y2)
            j += 1
        i += 1
    return min

def max(list):
    i = 0
    max = 0
    while i < len(list):
        j = 0
        l1 = re.split(' ', list[i])
        while j < len(list):
            l2 = re.split(' ', list[j])
            x1 = l1[0]
            y1 = l1[1]
            x2 = l2[0]
            y2 = l2[1]
            if hypotenuse(x1, y1, x2, y2) > max:
                max = hypotenuse(x1, y1, x2, y2)
            j += 1
        i += 1
    return max

def hypotenuse(X1, Y1, X2, Y2):
    res = [int(X1) - int(X2), int(Y1) - int(Y2)]

    return (res[0]**2 + res[1]**2)**(0.5)
file = open('C:\\Users\\nja_x\\AppData\\Local\\Programs\\Python\\Python35\\data.ex4')
myList = []

for line in file:
    myList.append(line.strip())
print("Task 5 | result: ")
print("max = ", max(myList))
print("min = ", min(myList, max(myList)))

file.close()
