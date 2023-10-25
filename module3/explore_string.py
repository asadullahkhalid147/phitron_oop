name = 'Sakib Khan'

# single quote diye start kora hole (\) diye (') use kora jae single quote er vitore
# this is called escape
name7 = 'Sakib\'s khan' 
name6 = "Sakib's khan"

name2 = "sakiB khan"

# multiline string
name3 = """  
    Sakib Khan
    number one
"""

name4 = "Sakib \n khan"
name5 = 'Sakib \n khan'

# string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
# slice in string
# string er index 1 theke 6 er ag porjonto
print(name2[1:6])


# negative index in string
print(name2[-3])

# reverse in string
print(name2[::-1])

# string er index a baire theke value set kora jae na
# name2[0]='R' // this will give error

# kono jinish string er vitor ase kina khub sohoje ber kora jae
if 'khan' in name2:
    print('exists')

## methods of string in python

# make all the letter UPPERCASE
print(name2.upper())

print(name2.lower())

print(name2.capitalize())

print(name2.title())

print(name2.swapcase())

# pdf file kina check kora jae endswith diye
print(name2.endswith('khan'))

# casefold buji nai
print(name2.casefold())

print(name2.count('a'))

#  format is important
age = 22
txt = "my name is {0} and i am {1} years old.{1} is a good number"
print(txt.format(name2,age))

ott = "i have {an:.2f}taka"
print(ott.format(an=4))
#  list is mutable. mutable means changeable. immutable means unchangeable

list1 = "hello"
print("#".join(list1))

string= "o ho my boy"
new = string.replace("boy","girl")

print(string.find('ho'))
print(new)
print(name7)