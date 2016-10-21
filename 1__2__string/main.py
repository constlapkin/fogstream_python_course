# task 2.1 with built-in functions

str = input("Task 2.1 | enter string: \n")

# task 2.1.1 lower case
str = str.lower()
str = str.capitalize()

# task 2.1.2 links

# task 2.1.3 emails

string = str
counter = list(string).count('@')
i = 0

while i < counter:
    index = string.find('@', 0, len(string)) 

    if index != len(string) and index != 0 and index != -1:
        if string[index - 1].isalpha() and string[index + 1].isalpha():
            Index = string.find('.', index, string.find(' ', index, len(string) - index))

            if Index != -1 and Index != len(string):
                if string[Index + 1].isalpha():
                    end = string.find(' ', Index, len(string) - Index)

                    if end == -1: 
                        end = len(string)

                    begin = string.rfind(' ', 0, index)

                    if begin == -1: 
                        begin = 0

                    string = string.replace(string[begin:end], '[контакты запрещены]')
    i += 1

str = string

# task 2.1.4 numbers
str = str.split(' ')
str = str [:]
for i in str:
    if i.isdigit() and len(i) >= 4:
        str.remove(i)
# str = ' '.join(str)
print(str)

# task 2.2 with regular expressions

import re
str = input("Task 2.2 | enter string: \n")

# task 2.2.1 lower case 
str = str.lower()
str = re.sub(r'^\w', str[:1].upper(), str)

# task 2.2.2 links

# task 2.2.3 emails
str = re.sub('\w+@\w+\.\w+','[контакты запрещены]', str)

# task 2.2.4 numbers
length = len(str)
str = re.sub('\d\d\d\d+', '', str)

print (str)
