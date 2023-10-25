num = int(input())

dictiionary={

}

for _ in range(1):
    numbers= list(map(int,input().split()))
    for i in numbers:
        if i in dictiionary:
            dictiionary[i]+=1
        else:
            dictiionary[i]=1

sum = 0
for key,value in dictiionary.items():
    if key <value:
        sum+=value-key
    elif key>value:
        sum+=value

print(sum)


