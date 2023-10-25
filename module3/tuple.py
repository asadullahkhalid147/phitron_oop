def multiple():
    return 3,4

# print(multiple())

things = 'pen','phone','bottle','charger','webcam'
print(things)
print(type(things))

print(things[0])
print(things[-2])
print(things[1:3])

# check
if 'phone' in things:
    print('exixts')

for item in things:
    print(item)

# tuple a baire theke index a insert korano jae na
# things[0]='wagon'

# tuple consist number of values separeted by commas
print(len(things))

# tuple of list
mega = ([2,3,4],[6,8,9,5])
print(type(mega))
# mega[0]=[55,11,2] // i can't to it because mega is a tuple

print(mega[0])
# tuple er vitore je list ase tar 1 no index a value insert korsi
mega[0][1]=666
print(mega[0])