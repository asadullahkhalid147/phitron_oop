# set: unique items collection: no duplicate
# list = []
# tuple = ()
# set= {}
numbers = [12,56,98,56,12,6,98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)
# same element can't be add more than one time
# do not maintain the sequence

# index does not exist in set
# print(numbers_set[2])

# do not set value from outside
# numbers_set[1]=5

numbers_set.remove(6)
print(numbers_set)

for item in numbers_set:
    print(item)

if 98 in numbers_set:
    print('exists')

A = {1,3,5}
B = {1,2,3,4,5}

print(A&B) #A^B

print(A|B) #A U B