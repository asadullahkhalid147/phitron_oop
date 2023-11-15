x,y = map(int,input().split())
arr=[]

for _ in range(1):
    cnt =0
    numbers= list(map(int,input().split()))
    for i in numbers:
        arr.append(i) 


count ={}
for i in range(1,y+1):
    count[i]=0

for j in arr:
    if j in count:
        count[j]+=1

for k,m in count.items():
    print(m)
