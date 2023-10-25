# def doubled(x):
#     return x*2
# we can write this function in one line

# here number is the name of parameter. ':' er por jei result pete chai sheta likhbo. we work here with one parameter
doubled = lambda num : num*2
squared = lambda num : num**2
result = doubled(44)
output = squared(9)
# print(result, output)

# if we use lambda with multiple parameter.
add = lambda x,y : x + y
sum = add(11,33)
print(sum)

# map
# map(je operation or function chalabo sheta, operation ba fuction jar upor chalabo she)
numbers = [12,56,98,56,12,6,98]
# doubled_nums = map(doubled,numbers)
doubled_nums = map(lambda x: x*2,numbers)
squared_nums = map(lambda x: x**2,numbers)
print(numbers)
print(list(doubled_nums))
print(list(squared_nums))

# map er output list akare nite hoy


actors = [
    {'name': 'sabana','age':65},
    {'name': 'sabnoor','age':45},
    {'name': 'sabila','age':30},
    {'name': 'srabonti','age':38},
    {'name': 'shaon','age':47},
]

# map holo sob gulor upor operation chalabe, ar filter holo condition thakbe, condition er upor based kore operation chalabe

juniors =  filter(lambda actor: actor['age']<40,actors)#ekhane condition holo actor er age 40 er niche hote hbe

fivers = filter(lambda actor: actor['age']%5==0,actors)
print(list(juniors))
print(list(fivers))