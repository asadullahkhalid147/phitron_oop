numbers = [12,56,98,56,12,6,98]

person = ['kala chan','kalipur',23,'student']

# key value pair or dictionary or object or hash table
# overlap with set

# {key:value, key:value, key:value}

person = {'name':'kala pakhi','address':'kalipur','age':23,'job':'facebook'}
print(person)
print(person['job'])
# name of property is a key
print(person.keys())
print(person.values())

# add new key with value
person['language']='python'
print(person)

# modify a key with new value
person['name']='sada chan'
print(person)

# delete a key with value
del person['age']
print(person)

# special dictionary loop
for key,value in person.items():
    print(key,value)

